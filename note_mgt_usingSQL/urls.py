from flask import Blueprint, session, jsonify, request, render_template

import config
from views import register, login, add_note, delete_note, edit_note, find_note, get_all_note, share_note
from views import login_required

bp = Blueprint('api', __name__)


@bp.post("/register")
def register_route():
    try:
        if request.method == 'POST':
            return register()
        #return render_template('index.html')
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@bp.post("/login")
def login_route():
    try:
        if request.method == 'POST':
            return login()
        #return render_template('login.html')
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@bp.post("/notes")
@login_required
def create_note_route():
    try:
        return add_note()
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@bp.delete("/delete")
@login_required
def delete_note_route():
    try:
        return delete_note()
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@bp.put("/update")
@login_required
def update_note_route():
    try:
        return edit_note()
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@bp.post("/get_note")
def get_note_route():
    try:
        return find_note()
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@bp.get("/notes")
@login_required
def get_all_notes_route():
    try:
        return get_all_note()
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@bp.post('/share_note')
@login_required
def share_note_route():
    return share_note()


@bp.post("/logout")
@login_required
def logout_route():
    session.pop('user_id', None)
    return jsonify({"message": "You are logged out"}), 200
