from flask import Blueprint, session, jsonify
from views import register, login, create_note, delete_note, update_note, get_note, get_all_notes
from views import login_required


bp = Blueprint('api', __name__)


@bp.route("/register", methods=['POST'])
def register_route():
    return register()


@bp.route("/login", methods=['POST'])
def login_route():
    return login()


@bp.route("/notes", methods=["POST"])
@login_required
def create_note_route():
    return create_note()


@bp.route("/delete", methods=["DELETE"])
@login_required
def delete_note_route():
    return delete_note()


@bp.route("/update", methods=["PUT"])
@login_required
def update_note_route():
    return update_note()


@bp.route("/get_note", methods=["POST"])
def get_note_route():
    return get_note()


@bp.route("/notes", methods=["GET"])
@login_required
def get_all_notes_route():
    return get_all_notes()


@bp.route("/logout", methods=["POST"])
@login_required
def logout_route():
    session.pop('user_id', None)
    return jsonify({"message": "You are logged out"}), 200
