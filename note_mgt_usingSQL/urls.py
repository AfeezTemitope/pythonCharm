from flask import Blueprint, session, jsonify, request, render_template
from views import register, login, add_note, delete_note, edit_note, find_note, get_all_note
from views import login_required

bp = Blueprint('api', __name__)


@bp.route("/register", methods=['POST'])
def register_route():
    try:
        if request.method == 'POST':
            return register()
        return render_template('index.html')
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@bp.route("/login", methods=['POST'])
def login_route():
    try:
        return login()
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@bp.route("/notes", methods=["POST"])
@login_required
def create_note_route():
    try:
        return add_note()
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@bp.route("/delete", methods=["DELETE"])
@login_required
def delete_note_route():
    try:
        return delete_note()
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@bp.route("/update", methods=["PUT"])
@login_required
def update_note_route():
    try:
        return edit_note()
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@bp.route("/get_note", methods=["POST"])
def get_note_route():
    try:
        return find_note()
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@bp.route("/notes", methods=["GET"])
@login_required
def get_all_notes_route():
    try:
        return get_all_note()
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@bp.route("/logout", methods=["POST"])
@login_required
def logout_route():
    session.pop('user_id', None)
    return jsonify({"message": "You are logged out"}), 200
