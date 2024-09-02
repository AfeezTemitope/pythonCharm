import bcrypt
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()
migrate = Migrate()


note_share = db.Table('note_share',
                      db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
                      db.Column('note_id', db.Integer, db.ForeignKey('note.id'), primary_key=True))

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

    def set_password(self, plain_password):
        self.password = bcrypt.hashpw(plain_password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    def check_password(self, plain_password):
        return bcrypt.checkpw(plain_password.encode('utf-8'), self.password.encode('utf-8'))

class Note(db.Model):
    __tablename__ = 'note'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    content = db.Column(db.Text, nullable=True)
    author = db.Column(db.String(120), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    owner = db.relationship('User', foreign_keys=[owner_id], backref=db.backref('notes_owned', lazy=True))
    shared_with = db.relationship('User', secondary=note_share,
                                  backref=db.backref('notes_shared', lazy='dynamic'))

class Count(db.Model):
    __tablename__ = 'count'

    name = db.Column(db.String(50), primary_key=True)
    count = db.Column(db.Integer, nullable=False)

def init_db(app):
    with app.app_context():
        db.create_all()
        if not Count.query.filter_by(name='user_id').first():
            new_count = Count(name='user_id', count=0)
            db.session.add(new_count)
            db.session.commit()
