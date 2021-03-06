"in future will use env variables for config"

DATABASE_URI = 'sqlite:///dbase\LFDB.db'
PROD_DATABASE_URI = 'postgres://gjhxidrwtohtsz:4d17d120d9014076d6640ef8cc11d38b14c014b55e39ac0852960bb3ea4fcd67@ec2-54-246-87-132.eu-west-1.compute.amazonaws.com:5432/dho17rloe03r7'
DEV_DATABASE_URI = 'sqlite:///dbase\LFDB.db'


class Config:
    """Base config."""
    # SECRET_KEY = environ.get('SECRET_KEY')
    # SESSION_COOKIE_NAME = environ.get('SESSION_COOKIE_NAME')

    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'
    SQLALCHEMY_DATABASE_URI = DATABASE_URI
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProdConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False

    # Database
    SQLALCHEMY_DATABASE_URI = PROD_DATABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False


class DevConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True

    # Database
    SQLALCHEMY_DATABASE_URI = DEV_DATABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
