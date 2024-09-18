from flask import Blueprint
from flask_cors import CORS
from flask_jwt_extended import JWTManager, jwt_required
from config import Config
from models import User, Task
from views import register, login, add_task, delete_task, share_task, get_tasks, get_profile, update_profile, edit_task

todo_bp = Blueprint('todoApp', __name__)
todo_bp.secret_key = Config.SECRET_KEY
CORS(todo_bp, supports_credentials=True)


@todo_bp.post('/register')
def register_route():
    return register()


@todo_bp.post('/login')
def login_route():
    return login()


@todo_bp.post('/add_task')
@jwt_required
def add_task_route():
    return add_task()


@todo_bp.delete('/delete_task')
@jwt_required
def delete_route():
    return delete_task()


@todo_bp.post('/share')
@jwt_required
def share_route():
    return share_task()


@todo_bp.get('/get_task')
@jwt_required
def get_route():
    return get_tasks()


@todo_bp.post('/update')
@jwt_required
def update_user_profile():
    return update_profile()


@todo_bp.get('/user_profile')
@jwt_required
def get_user_profile():
    return get_profile()


@todo_bp.post('/edit_task')
@jwt_required
def edit_task_route():
    return edit_task()