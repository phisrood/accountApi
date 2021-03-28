from api import db, ma
from datetime import datetime

class Account(db.Model):
    __table__name__ = 'account'
    user_id = db.Column(db.String, primary_key=True)
    password = db.Column(db.String)
    user_name = db.Column(db.String)
    email = db.Column(db.String)
    email_auth_yn = db.Column(db.String)
    sns_reg_div = db.Column(db.String)
    mobile_number = db.Column(db.String)
    created_at = db.Column(db.String)
    updated_at = db.Column(db.String)

    def __init__(self,user_id,password,user_name,email,mobile_number):
        self.user_id = user_id
        self.password = password
        self.user_name = user_name
        self.email = email
        self.email_auth_yn = 'N'
        self.sns_reg_div = 'web'
        self.mobile_number = mobile_number
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

class AccountSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Account

    user_id = ma.auto_field()
    user_name = ma.auto_field()
    email = ma.auto_field()
    mobile_number = ma.auto_field()
    email_auth_yn = ma.auto_field()
