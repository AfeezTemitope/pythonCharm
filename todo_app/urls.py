from flask import Blueprint
from flask_cors import CORS

from views import register, login, add_task, login_required, delete_task, share_task, get_tasks, get_profile, \
    update_profile, edit_task

bp = Blueprint('todo', __name__)
CORS(bp)


@bp.post('/register')
def register_route():
    return register()


@bp.post('/login')
def login_route():
    return login()


@bp.post('/add_task')
@login_required
def add_task_route():
    return add_task()


@bp.post('/delete')
@login_required
def delete_route():
    return delete_task()


@bp.post('/share')
@login_required
def share_route():
    return share_task()


@bp.get('/get')
@login_required
def get_route():
    return get_tasks()


@bp.post('/update')
@login_required
def update_user_profile():
    return update_profile()


@bp.get('/user_profile')
@login_required
def get_user_profile():
    return get_profile()


@bp.post('/edit_task')
@login_required
def edit_task_route():
    return edit_task()
