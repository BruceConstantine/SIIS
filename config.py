import os


class Config:
    def __init__(self):
        pass

    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    DEBUG = True

    @staticmethod
    def init_app(app):
        pass


config = {'default': Config}
