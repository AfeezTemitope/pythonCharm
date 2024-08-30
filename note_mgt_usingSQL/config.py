import os


class Config:
    SECRET_KEY = 'secret'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:t3m1t%40p3@localhost:3306/note_mgt'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
