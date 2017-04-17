import os
basedir = os.path.abspath(os.path.dirname(__file__))


class DevelopmentConfig(object):
    DEBUG = True
    SECRET_KEY = 'Test_TA'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

