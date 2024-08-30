import bcrypt
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)  # Adjusted length for bcrypt

    def set_password(self, plain_password):
        self.password = bcrypt.hashpw(plain_password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    def check_password(self, plain_password):
        return bcrypt.checkpw(plain_password.encode('utf-8'), self.password.encode('utf-8'))


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    content = db.Column(db.Text, nullable=True)
    author = db.Column(db.String(120), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now().strftime("%Y-%m-%d"))


class Count(db.Model):
    name = db.Column(db.String(50), primary_key=True)
    count = db.Column(db.Integer, nullable=False)


def init_db(app):
    with app.app_context():
        db.create_all()  # Create tables
        if not Count.query.filter_by(name='user_id').first():
            new_count = Count(name='user_id', count=0)
            db.session.add(new_count)
            db.session.commit()
