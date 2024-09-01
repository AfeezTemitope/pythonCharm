import os


class Config:
    SECRET_KEY = 'SECRET_KEY'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'mysql+pymysql://root:t3m1t%40p3@localhost:3306/contact_mgt'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
