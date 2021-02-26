import os


UPLOAD_FOLDER = '/excel/uploads'


class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DB_CREDENTIALS")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = UPLOAD_FOLDER
    SECRET_KEY = os.getenv("SECRET_KEY")
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True


class ProductionConfig(Config):
    DEBUG = False


# class StagingConfig(Config):
#     DEVELOPMENT = True
#     DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


# class TestingConfig(Config):
#     TESTING = True
