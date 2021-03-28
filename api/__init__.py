from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flasgger import Swagger
from config import config as Config
from flask_mail import Mail

db = SQLAlchemy()
ma = Marshmallow()
api = Api()
swagger = Swagger(template_file='components.json',parse=True)
#mail = Mail()

def create_app():
    app = Flask(__name__)
    config_name = 'default'
    app.config.from_object(Config[config_name])

    db.init_app(app)
    ma.init_app(app)
    api.init_app(app)
    #mail.init_app(app)

    return app


from api.resource.routes import init_routes
init_routes(api)