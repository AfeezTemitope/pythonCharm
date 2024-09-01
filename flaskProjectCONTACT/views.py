import bcrypt
from flask import request, jsonify, session
from functools import wraps
from models import db, Contact, User


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return jsonify({"message": "You are not logged in"}), 401
        return f(*args, **kwargs)

    return decorated_function


def register():
    data = request.get_json()
    name = data.get('name', '').strip().lower()
    password = data.get('password', '').strip()

    if not name or not password:
        return jsonify({"message": "Name or password cannot be empty"}), 400

    if User.query.filter_by(name=name).first():
        return jsonify({"message": "Name already exists"}), 400

    user = User(name=name)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "User registered successfully"}), 201


def login():
    data = request.get_json()
    name = data['name'].strip().lower()
    password = data['password'].strip()
    user = User.query.filter_by(name=name).first()
    if user and user.check_password(password):
        session['user_id'] = user.id
        return jsonify({"message": "login successful"}), 200
    else:
        return jsonify({"message": "invalid username or password"}), 400



def add_contact():
    data = request.get_json()
    name = data.get('name', '').strip()
    phone_number = data.get('phone_number', '').strip()

    if not validate_number(phone_number):
        return jsonify({'message': 'Invalid phone number'}), 400

    existing_contact = Contact.query.filter_by(phone_number=phone_number, user_id=session['user_id']).first()
    if existing_contact:
        return jsonify({'message': 'Contact already exists'}), 400

    new_contact = Contact(name=name, phone_number=phone_number, user_id=session['user_id'])
    db.session.add(new_contact)
    db.session.commit()
    return jsonify({'message': 'Contact added'}), 201


def delete_contact(phone_number):
    contact = Contact.query.filter_by(phone_number=phone_number, user_id=session['user_id']).first()
    if not contact:
        return jsonify({'message': 'Contact not found'}), 404

    db.session.delete(contact)
    db.session.commit()
    return jsonify({'message': 'Contact deleted'}), 200


def update_contact():
    data = request.get_json()
    old_phone_number = data.get('old_phone_number', '').strip()
    new_phone_number = data.get('new_phone_number', '').strip()

    if not old_phone_number:
        return jsonify({'message': 'Old phone number is required'}), 400

    contact = Contact.query.filter_by(phone_number=old_phone_number, user_id=session['user_id']).first()
    if contact:
        contact.name = data.get('name', contact.name)
        if new_phone_number:
            contact.phone_number = new_phone_number
        db.session.commit()
        return jsonify({'message': 'Contact updated'}), 200
    else:
        return jsonify({'message': 'Contact not found'}), 404


def get_contact(phone_number):
    contact = Contact.query.filter_by(phone_number=phone_number, user_id=session['user_id']).first()
    if contact:
        return jsonify({
            'message': 'Contact found',
            'contact': contact.to_dict()
        }), 200
    else:
        return jsonify({'message': 'Contact not found'}), 404


def get_all_contacts():
    try:
        contacts = Contact.query.filter_by(user_id=session['user_id']).all()
        return jsonify({'contacts': [contact.to_dict() for contact in contacts]}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


def validate_number(number):
    return number.isdigit() and len(number) in [10, 11]
