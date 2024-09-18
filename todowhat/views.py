from flask import request, jsonify

# from app import jwt
from models import User, db, Task, BLOCKLIST
from flask_jwt_extended import create_access_token, get_jwt_identity, get_jwt


def validate_password_length(password):
    if len(password) < 6:
        return False, "Password must be at least 6 characters"
    return True, ""


def register():
    data = request.get_json()
    username = data.get('username', '').strip().lower()
    password = data.get('password', '').strip()

    if not username or not password:
        return jsonify({'message': 'Username and password are required'}), 400
    is_valid, msg = validate_password_length(password)
    if not is_valid:
        return jsonify({'message': msg}), 400
    if User.query.filter_by(username=username).first():
        return jsonify({'message': 'User already exists'}), 400
    user = User(username=username)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully'}), 201


def login():
    data = request.get_json()
    username = data.get('username', '').strip().lower()
    password = data.get('password', '').strip()
    user = User.query.filter_by(username=username).first()

    if user and user.check_password(password):
        access_token = create_access_token(identity=user.id)
        return jsonify(access_token=access_token, message="Logged in successfully"), 200
    else:
        return jsonify({'message': 'Invalid username or password'}), 400


def add_task():
    user_id = get_jwt_identity()
    data = request.get_json()

    new_task = Task.from_dict(data, user_id)

    if not new_task.title:
        return jsonify({"message": 'title cannot be empty'}), 400

    existing_task = Task.query.filter_by(title=new_task.title, user_id=user_id).first()
    if existing_task:
        return jsonify({"message": 'Task already exists'}), 400

    db.session.add(new_task)
    try:
        db.session.commit()
        return jsonify({"message": "Task added successfully"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": "Failed to add task", "error": str(e)}), 500


def delete_task():
    user_id = get_jwt_identity()
    data = request.get_json()
    task_id = data.get('task_id')
    task = Task.query.filter_by(id=task_id, user_id=user_id).first()
    if task:
        db.session.delete(task)
        db.session.commit()
        return jsonify({"message": "task deleted successfully"}), 200
    return jsonify({'message' : "Task not found"}), 400


def edit_task():
    user_id = get_jwt_identity()
    data = request.get_json()
    task_id = data.get('task_id')
    new_title = data.get('title', '').strip()
    new_description = data.get('description', '').strip()

    task = Task.query.filter_by(id=task_id, user_id=user_id).first()
    if not task:
        return jsonify({"Task not found"}), 404

    if new_title:
        existing_task = Task.query.filter_by(title=new_title, user_id=user_id).first()
        if existing_task and existing_task.id != task_id:
            return jsonify({"Task with this title already exists"}), 400
        task.title = new_title
    if new_description:
        task.description = new_description

    db.session.commit()
    return jsonify({"message" : "Task updated successfully"}), 200


def search_task():
    user_id = get_jwt_identity()
    title = request.args.get('title', '').strip()

    tasks = Task.query.filter(Task.user_id == user_id, Task.title.like(f'%{title}%')).all()
    if not tasks:
        return jsonify({"message": "No tasks found"}), 404

    tasks_data = [{"task_id": task.id, "title": task.title, "description": task.description} for task in tasks]
    return jsonify({"tasks": tasks_data}), 200


def share_task():
    var = get_jwt_identity()
    data = request.get_json()
    task_id = data.get('task_id')
    user_id = data.get('user_id')
    task = Task.query.filter_by(id=task_id, user_id=var).first()
    user_to_share_with = User.query.get(user_id)
    if task and user_to_share_with:
        task.shared_tasks.append(user_to_share_with)
        db.session.commit()
        return jsonify({"message": "task shared successfully"}), 200
    return "Task not found", 400


def get_tasks():
    user_id = get_jwt_identity()
    tasks = Task.query.filter_by(user_id=user_id).all()
    task_list = [{"task_id": task.id, "title": task.title, "description": task.description} for task in tasks]
    return jsonify({"tasks": task_list}), 200


def update_profile():
    user_id = get_jwt_identity()
    data = request.get_json()
    bio = data.get('bio', '').strip()
    profile_picture = data.get('profile_picture', '').strip()

    user = User.query.get(user_id)
    if not user:
        return jsonify({"message": "User not found"}), 404

    user.bio = bio
    user.profile_picture = profile_picture
    db.session.commit()
    return jsonify({"Profile updated successfully": "message"}), 200


def get_profile():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user:
        return jsonify({"User not found"}), 404

    profile = {
        "username": user.username,
        "bio": user.bio,
        "profile_picture": user.profile_picture
    }
    return {"profile": profile}, 200


def logout():
    jti = get_jwt()['jti']
    BLOCKLIST.add(jti)
    return jsonify({"msg": "Successfully logged out"}), 200





