from datetime import datetime

import bcrypt
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
BLOCKLIST = set()


task_user = db.Table('task_user',
    db.Column('task_id', db.Integer, db.ForeignKey('task.id'), primary_key=True),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True)
)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(180), nullable=False)
    tasks = db.relationship('Task', backref='user', lazy=True)
    bio = db.Column(db.String(500), nullable=True)
    profile_picture = db.Column(db.String(255), nullable=True)

    def __repr__(self):
        return f'<User {self.username}>'

    def set_password(self, plain_password):
        self.password = bcrypt.hashpw(plain_password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    def check_password(self, plain_password):
        return bcrypt.checkpw(plain_password.encode('utf-8'), self.password.encode('utf-8'))


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80),  nullable=False)
    description = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    #completion = db.Column(db.DateTime, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    shared_tasks = db.relationship('User', secondary='task_user', backref='shared_tasks')

    def __init__(self, title, description, user_id):
        self.title = title
        self.description = description
        self.user_id = user_id

    @classmethod
    def from_dict(cls, data, user_id):
        task_data = data.get('title', {})
        title = task_data.get('title')
        description = task_data.get('description', '').strip()
        return cls(title=title, description=description, user_id=user_id)

    def __repr__(self):
        return f'<Task {self.title}>'
