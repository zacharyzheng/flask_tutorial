import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = 'zachary@a9182HE'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://debian-sys-maint:AmZam5dO7i5uC0fW@localhost:3306/flaskblog?charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
