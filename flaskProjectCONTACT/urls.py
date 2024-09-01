from flask import Blueprint
from views import add_contact, delete_contact, update_contact, get_all_contacts, get_contact, login_required, register, \
    login

bp = Blueprint('app', __name__)


@bp.route("/register", methods=['POST'])
def register_route():
    return register()


@bp.route("/login", methods=['POST'])
def login_route():
    return login()


@bp.route("/add_contact", methods=['POST'])
@login_required
def add_contact_route():
    return add_contact()


@bp.route("/delete_contact/<string:phone_number>", methods=['DELETE'])
@login_required
def delete_contact_route(phone_number):
    return delete_contact(phone_number)


@bp.route("/update_contact", methods=['PUT'])
@login_required
def update_contact_route():
    return update_contact()


@bp.route("/get_contact/<string:phone_number>", methods=['GET'])
@login_required
def get_contact_route(phone_number):
    return get_contact(phone_number)


@bp.route("/get_all_contacts", methods=['GET'])
@login_required
def get_all_contacts_route():
    return get_all_contacts()

