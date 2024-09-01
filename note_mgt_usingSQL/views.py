from datetime import datetime
from functools import wraps
from flask import request, jsonify, session, redirect, url_for, flash

from models import Count, db, User, Note


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return jsonify({"message": "You are not logged in"}), 401
        return f(*args, **kwargs)
    return decorated_function


def generate_id():
    count = Count.query.filter_by(name='user_id').first()
    if not count:
        count = Count(name='user_id', count=0)
        db.session.add(count)
    count.count += 1
    return count.count


def register():
    data = request.get_json()
    username = data.get('username', '').strip().lower()
    password = data.get('password', '').strip()
    if not username or not password:
        return "username or password cannot be empty", 400

    if User.query.filter_by(username=username).first():
        return "username already exist", 400

    user_id = generate_id()
    user = User(id=user_id, username=username)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    return jsonify("user created successfully"), 201
    #return jsonify({"message": "user created"}), 201


def login():
    data = request.get_json()
    username = data['username'].strip().lower()
    password = data['password'].strip()
    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        session['user_id'] = user.id
        return jsonify({"message": "login successful"}), 200
    else:
        return jsonify({"message": "invalid username or password"}), 400


def add_note():
    data = request.get_json()
    user_id = session['user_id']
    title = data['title'].strip()
    if not title:
        return jsonify({"message": "title cannot be empty"}), 400
    existing_notes = Note.query.filter_by(title=title, user_id=user_id).first()
    if existing_notes:
        return jsonify({"message": "note already exists"}), 400
    new_note = Note(id=generate_id(), title=title, content=data['content'], author=data['author'], user_id=user_id,
                    created_at=datetime.now().strftime("%Y-%m-%d"))
    db.session.add(new_note)
    db.session.commit()
    return jsonify({"message": "note created"}), 201


def delete_note():
    data = request.get_json()
    user_id = session['user_id']
    note_id = data['note_id']
    note = Note.query.filter_by(id=note_id, user_id=user_id).first()
    if note:
        db.session.delete(note)
        db.session.commit()
        return jsonify({"message": "note deleted"}), 200
    else:
        return jsonify({"message": "note not found"}), 400


def edit_note():
    data = request.get_json()
    user_id = session['user_id']
    note_id = data['note_id']
    title = data['title'].strip()
    content = data['content'].strip()
    note = Note.query.filter_by(id=note_id, user_id=user_id).first()
    if note:
        note.title = title
        note.content = content
        db.session.commit()
        return jsonify({"message": "note updated"}), 200
    else:
        return jsonify({"message": "note not found"}), 400


def find_note():
    data = request.get_json()
    title = data['title'].strip()
    user_id = data['user_id']
    if title:
        if user_id:
            note = Note.query.filter_by(title=title, user_id=user_id).first()
        else:
            note = Note.query.filter_by(title=title).first()
        if note:
            return jsonify({"message": "note found", "note": note.as_dict()}), 200
        else:
            return jsonify({"message": "note not found"}), 400
    else:
        return jsonify({"message": "title cannot be empty"}), 400


def get_all_note():
    user_id = session['user_id']
    limit = int(request.args.get('limit', 10))
    notes_list = Note.query.filter_by(user_id=user_id).limit(limit).all()
    if notes_list:
        return jsonify({"notes": [note.as_dict() for note in notes_list]}), 200
    else:
        return jsonify({"message": "note not found"}), 400


def note_as_dict(self):
    return {
        "id": self.id,
        "title": self.title,
        "content": self.content,
        "author": self.author,
        "user_id": self.user_id,
        "created_at": self.created_at.strftime("%Y-%m-%d")
    }


Note.as_dict = note_as_dict
