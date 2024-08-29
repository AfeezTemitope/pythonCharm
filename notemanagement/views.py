from datetime import datetime
from flask import jsonify, request, session
from functools import wraps
from models import users, notes, generate_id
from werkzeug.security import generate_password_hash, check_password_hash


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return jsonify({"message": "You are not logged in"}), 401
        return f(*args, **kwargs)
    return decorated_function


def register():
    data = request.get_json()
    username = data['username'].strip().lower()
    password = data['password'].strip()
    if not username or not password:
        return jsonify({"message": "Username and password cannot be empty"}), 400
    if users.find_one({"username": username}):
        return jsonify({"message": "Username already registered"}), 400
    hashed_password = generate_password_hash(password)
    user_id = generate_id()
    user = {"_id": user_id, "username": username, "password": hashed_password}
    users.insert_one(user)
    return jsonify({"message": "User created successfully", "user_id": user_id}), 201


def login():
    data = request.get_json()
    username = data['username'].strip().lower()
    password = data['password'].strip()
    user = users.find_one({"username": username})
    if user and check_password_hash(user["password"], password):
        session['user_id'] = str(user["_id"])
        return jsonify({"message": "Logged in successfully"}), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 401


def create_note():
    data = request.get_json()
    user_id = session['user_id']
    title = data['title']
    if not title:
        return jsonify({"message": "Title cannot be empty"}), 400
    existing_note = notes.find_one({"title": title, "user_id": user_id})
    if existing_note:
        return jsonify({"message": "Note already exists"}), 400
    new_note = {"_id": generate_id(), "title": data['title'], "content": data['content'], "author": data['author'],
                "user_id": user_id, "created_at": datetime.now().strftime("%Y-%m-%d")}
    notes.insert_one(new_note)
    return jsonify({"message": "Note created", "note_id": new_note["_id"]}), 200


def delete_note():
    data = request.get_json()
    user_id = session['user_id']
    note_id = data['note_id']
    if notes.find_one({"_id": note_id, "user_id": user_id}):
        notes.delete_one({"_id": note_id, "user_id": user_id})
        return jsonify({"message": "Note deleted"}), 200
    else:
        return jsonify({"message": "Note not found"}), 404


def update_note():
    data = request.get_json()
    user_id = session['user_id']
    note_id = data['note_id']
    title = data['title']
    content = data['content']
    if notes.find_one({"_id": note_id, "user_id": user_id}):
        notes.update_one({"_id": note_id, "user_id": user_id}, {"$set": {"title": title, "content": content}})
        return jsonify({"message": "Note updated"}), 200
    else:
        return jsonify({"message": "Note not found"}), 404


def get_note():
    data = request.get_json()
    title = data.get("title")
    user_id = data.get("user_id")

    if title:
        if user_id:
            note = notes.find_one({"title": title, "user_id": user_id})
        else:
            note = notes.find_one({"title": title})
        if note:
            return jsonify({"message": "Note found", "note": note}), 200
        else:
            return jsonify({"message": "Note not found"}), 404
    else:
        return jsonify({"message": "Title parameter is required"}), 400


def get_all_notes():
    user_id = session['user_id']
    limit = int(request.args.get('limit', 10))
    notes_list = notes.find({"user_id": user_id}).limit(limit)
    notes_list = list(notes_list)
    if notes_list:
        return jsonify({"message": "Notes found", "notes": notes_list}), 200
    else:
        return jsonify({"message": "No notes found for this user"}), 404

