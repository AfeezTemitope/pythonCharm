from functools import wraps

from flask import session, request, jsonify

from models import User, db, Task


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return "message: You are not logged in", 401
        return f(*args, **kwargs)

    return decorated_function


def register():
    data = request.get_json()
    username = data.get('username', '').strip().lower()
    password = data.get('password', '').strip()
    if not username or not password:
        return jsonify({"message": "Missing username or password"}), 400
    if User.query.filter_by(username=username).first():
        return jsonify({"message": 'Username is already taken'}), 400
    user = User(username=username)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": f'user {username} now has a todo list'}), 201


def login():
    data = request.get_json()
    username = data.get('username', '').strip().lower()
    password = data.get('password', '').strip()
    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        session['user_id'] = user.id
        return jsonify({"message": "logged in successfully"}), 200
    else:
        return jsonify({'message': 'Invalid username or password'}), 400


def add_task():
    data = request.get_json()
    title = data.get('title', '').strip()
    description = data.get('description', '').strip()
    user_id = session['user_id']
    if not title:
        return jsonify({"message":'title cannot be empty'}), 400
    existing_task = Task.query.filter_by(title=title, user_id=user_id).first()
    if existing_task:
        return jsonify({"message": 'Task already exists'}), 400
    new_task = Task(title, description, user_id)
    db.session.add(new_task)
    db.session.commit()
    return jsonify({"message": "Task added successfully"}), 200


def delete_task():
    data = request.get_json()
    user_id = session['user_id']
    task_id = data.get('task_id')
    task = Task.query.filter_by(id=task_id, user_id=user_id).first()
    if task:
        db.session.delete(task)
        db.session.commit()
        return "task deleted successfully", 200
    else:
        return "Task not found", 400


def edit_task():
    data = request.get_json()
    task_id = data.get('task_id')
    new_title = data.get('title', '').strip()
    new_description = data.get('description', '').strip()
    user_id = session['user_id']

    task = Task.query.filter_by(id=task_id, user_id=user_id).first()
    if not task:
        return "Task not found", 404

    if new_title:
        existing_task = Task.query.filter_by(title=new_title, user_id=user_id).first()
        if existing_task and existing_task.id != task_id:
            return "Task with this title already exists", 400
        task.title = new_title
    if new_description:
        task.description = new_description

    db.session.commit()
    return "Task updated successfully", 200


def share_task():
    data = request.get_json()
    var = session['user_id']
    task_id = data.get('task_id')
    user_id = data.get('user_id')
    task = Task.query.filter_by(id=task_id, user_id=var).first()
    user_to_share_with = User.query.get(user_id)
    if task and user_to_share_with:
        task.shared_tasks.append(user_to_share_with)
        db.session.commit()
        return "task shared successfully", 200
    return "Task not found", 400


def get_tasks():
    user_id = session['user_id']
    tasks = Task.query.filter_by(user_id=user_id).all()
    task_list = [{"task_id": task.id, "title": task.title, "description": task.description} for task in tasks]
    return {"tasks": task_list}, 200


def update_profile():
    data = request.get_json()
    bio = data.get('bio', '').strip()
    profile_picture = data.get('profile_picture', '').strip()

    user_id = session['user_id']
    user = User.query.get(user_id)
    if not user:
        return "User not found", 404

    user.bio = bio
    user.profile_picture = profile_picture
    db.session.commit()
    return "Profile updated successfully", 200


def get_profile():
    user_id = session['user_id']
    user = User.query.get(user_id)
    if not user:
        return "User not found", 404

    profile = {
        "username": user.username,
        "bio": user.bio,
        "profile_picture": user.profile_picture
    }
    return {"profile": profile}, 200


