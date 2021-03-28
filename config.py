import logging


class Config:
    from swagger import swagger_config
    SWAGGER = swagger_config

    @staticmethod
    def init_app(app):
        pass


class DevConfig(Config):
    DEBUG = True
    HOST = '0.0.0.0'

    SQLALCHEMY_DATABASE_URI = 'postgresql://kguru:Kcnet00!@#$@180.64.50.38:5432/account'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True

    #메일 설정
    """
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = '587'
    MAIL_USERNAME = 'kymDev0124@gmail.com'
    MAIL_PASSWORD = 'qkcnlldrijkkdvqd'
    MAIL_USE_TLS = True
    """

    # logging config
    logging.basicConfig(level=logging.INFO,format='%(levelname)s:%(pathname)s>%(message)s')

    @classmethod
    def init_app(cls, app):
        print('[Dev config]This app is in debug mode')


config = {
    'dev': DevConfig,
    'default': DevConfig
}