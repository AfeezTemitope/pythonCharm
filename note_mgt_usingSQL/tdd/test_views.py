import unittest
from app import app, db


class NoteTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = app
        cls.client = cls.app.test_client()
        cls.app.config['TESTING'] = True
        cls.app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:t3m1t%40p3@localhost:3306/note_mgt'
        cls.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        with cls.app.app_context():
            db.create_all()

    @classmethod
    def tearDownClass(cls):
        with cls.app.app_context():
            db.drop_all()
