from flask import request, jsonify
from flask_restful import Resource
from api.model.account import Account, AccountSchema

from api import db
from sqlalchemy.exc import IntegrityError
from api.resource import account_util

account_schema = AccountSchema()

class AccountApi(Resource):
    def get(self, user_id):
        account = Account.query.filter_by(user_id=user_id).first()
        return jsonify(account_schema.dump(account))

    def delete(self, user_id):
        deleted_account = Account.query.filter_by(user_id=user_id).first()
        if deleted_account is None:
            return {
                       "message": "Account not found"
                   }, 404

        try:
            db.session.delete(deleted_account)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()

            return {
                       "message": "IntegrityError on deleting user"
                   }, 409
        return {
            "message": "Successfully deleted user profile"
        }


class AccountsApi(Resource):
    def get(self):
        query_result = Account.query.all()
        accounts = [account_schema.dump(account) for account in query_result]
        return jsonify(accounts)


class AccountRegisterApi(Resource):
    def post(self):
        print("회원등록")
        exist_account = Account.query.filter_by(user_id=request.args['user_id']).first()
        if exist_account is not None:
            print("Account is already exists")
            return {
                "message": "This user id is already exists"
            }

        new_account = Account(
            user_id=request.args['user_id'],
            password=request.args['password'],
            user_name=request.args['user_name'],
            email=request.args['email'],
            mobile_number=request.args['mobile_number']
        )

        new_account.password = account_util.encryptPassword(new_account.password).decode("UTF-8");
        db.session.add(new_account)

        try:
            db.session.commit()
            account_util.send_email(new_account)
        except IntegrityError:
            db.session.rollback()
            return {
                "message": "Fail to register user because of IntegrityError on db"
            }

        return account_schema.dump(new_account)

class AccountAuthApi(Resource):
    def get(self):
        exist_account = Account.query.filter_by(user_id=request.args['user_id']).first()
        if exist_account is None:
            print("Account is None")
            return {
                "message": "This user id is None"
            }

        exist_account.email_auth_yn = 'Y'

        try:
            db.session.commit()
            print("auth success")
        except IntegrityError:
            db.session.rollback()
            return {
                "message": "Fail to register user because of IntegrityError on db"
            }

        return {
                   "message": "Mail Authorization complete"
               }, 200

