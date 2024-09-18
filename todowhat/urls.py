from flask import Blueprint
from flask_cors import CORS
from flask_jwt_extended import jwt_required
from config import Config

from views import register, login, add_task, delete_task, share_task, get_tasks, get_profile, update_profile, edit_task, \
    logout, search_task

todo_bp = Blueprint('todoApp', __name__)
todo_bp.secret_key = Config.SECRET_KEY
CORS(todo_bp, supports_credentials=True)


@todo_bp.route('/register', methods=['POST'], endpoint='register')
def register_route():
    return register()


@todo_bp.route('/login', methods=['POST'], endpoint='login')
def login_route():
    return login()


@todo_bp.route('/add_task', methods=['POST'], endpoint='add_task')
@jwt_required()
def add_task_route():
    return add_task()


@todo_bp.route('/delete_task', methods=['DELETE'], endpoint='delete_task')
@jwt_required()
def delete_route():
    return delete_task()


@todo_bp.route('/search_task', methods=['GET'])
@jwt_required()
def search_task_route():
    return search_task()


@todo_bp.route('/share', methods=['POST'], endpoint='share_task')
@jwt_required()
def share_route():
    return share_task()


@todo_bp.route('/get_task', methods=['GET'], endpoint='get_task')
@jwt_required()
def get_route():
    return get_tasks()


@todo_bp.route('/update', methods=['PUT'], endpoint='update_profile')
@jwt_required()
def update_user_profile():
    return update_profile()


@todo_bp.route('/user_profile', methods=['GET'], endpoint='get_profile')
@jwt_required()
def get_user_profile():
    return get_profile()


@todo_bp.route('/edit_task', methods=['POST'], endpoint='edit_task')
@jwt_required()
def edit_task_route():
    return edit_task()


@todo_bp.route('/logout', methods=['POST'], endpoint='logout')
@jwt_required()
def logout_route():
    return logout()