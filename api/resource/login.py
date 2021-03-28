from flask import request, Response
from flask_restful import Resource
from api.model.account import Account
from datetime import datetime, timedelta
import jwt

from api.resource import account_util
from functools import wraps

class loginApi(Resource):
    def post(self):
        exist_account = Account.query.filter_by(user_id=request.args['user_id']).first()

        if exist_account is None:
            return {
                "message": "ID Not Found"
            }, 403
        else:

            if account_util.checkPassword(sourcePassword=exist_account.password, inputPassword=request.args['password']):
                user_id = exist_account.user_id
                payload = {
                    "user_id": user_id,
                    "exp": datetime.utcnow() + timedelta(seconds=60 * 60 * 24)
                }

                token = jwt.encode(payload, "secretkey", "HS256")
                print(token)
                return {
                    "Authorization":  token
                }, 200
            else:
                return {
                           "message": "ID or Password do not match"
                       }, 403

class authorizationApi(Resource):
    def post(self):
        access_token = request.headers.get("Authorization")
        id = request.args['user_id']
        if access_token is not None:
            try:
                payload = jwt.decode(access_token, "secretkey", "HS256")
            except jwt.InvalidTokenError:
                payload = None

            if payload is None:
                return {
                           "message": "Authorization Failed(Invalid access_token)"
                       }, 403

            user_id = payload["user_id"]

            if user_id == id:
                return {
                           "message": "Authorization success",
                            "user_id": user_id
                       }, 200
            else:
                return {
                           "message": "Authorization Failed(user id do not match)"
                       }, 403
        else:
            return {
                           "message": "Authorization Failed(access_token is none)"
                       }, 403

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        access_token = request.headers.get("Authorization")
        if access_token is not None:
            try:
                payload = jwt.decode(access_token, "secretkey", "HS256")
            except jwt.InvalidTokenError:
                payload = None

            if payload is None:
                return Response(status=401)

            user_id = payload["user_id"]

            if user_id == id:
                print("login success")
            else:
                print("login falied")
        else:
            return Response(status=401)

        return f(*args,**kwargs)
    return decorated_function

