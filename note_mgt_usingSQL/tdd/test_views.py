import unittest
from app import app, db
from models import User


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

    def setUp(self):
        with self.app.app_context():
            self.user = User(username='badbby', password='password')
            self.user.set_password('badbby')
            db.session.add(self.user)
            db.session.commit()
            self.client.post('/login', json={'username': '', 'badbby': 'password'})
            self.session_cookie = self.client.cookie_jar._cookies['localhost.local'][b'/']['session']

    def test_register(self):
        response = self.client.post('/register', json={'username': 'bello', 'password': '123456'})
        self.assertEqual(response.status_code, 201)
        self.assertIn(b'user created successfully', response.data)

    def test_login(self):
        response = self.client.post('/login', json={'username': 'bello', 'password': '123456'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'login successful', response.data)
