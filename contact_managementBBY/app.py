from flask import Flask, jsonify, request
from pymongo import MongoClient


app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017')
aleroDB = client['big_boy']


@app.route("/add_contact", methods=['POST'])
def add_contact():
    data = request.get_json()
    name = data.get('name').strip().lower()
    phone_number = data.get('phone_number')
    validate_number(phone_number)

    existing_number = aleroDB.contacts.find_one({'phone_number': phone_number})
    if existing_number:
        return jsonify({'message': 'Contact already exists'}), 400
    else:
        new_contact = {'name': name, 'phone_number': phone_number}
        aleroDB.contacts.insert_one(new_contact)
        return jsonify({'message': 'Contact added'}), 201


def validate_number(number):
    if number == 11 and number.isdigit():
        return number


@app.route("/delete_contact/<int:phone_number>", methods=['DELETE'])
def delete_contact(phone_number):
    contact = aleroDB.contacts.delete_one({'phone_number': phone_number})
    if not contact:
        return jsonify({'message': 'Contact not found'}), 404
    else:
        return jsonify({'message': 'Contact deleted'}), 200


@app.route("/update_contact/<int:phone_number>", methods=['PUT'])
def update_contact(phone_number):
    data = request.get_json()
    contact = aleroDB.contacts.find_one({'phone_number': phone_number})
    if not contact:
        return jsonify({"message": "Contact not found"}), 404
    else:
        name = data.get('name').strip().lower()
        aleroDB.contacts.update_one({'phone_number': phone_number}, {"$set": {'name': name}})
        return jsonify({'message': 'Contact updated'}), 200


@app.route("/get_contact/<int:phone_number>", methods=['GET'])
def get_contact(phone_number):
    contact = aleroDB.contacts.find_one({'phone_number': phone_number})
    if contact:
        return jsonify({
            'message': 'Contact found',
            'contact': {
                'name': contact['name'], 'phone_number': contact['phone_number']
            }
        }), 200
    else:
        return jsonify({'message': 'Contact not found'}), 404


@app.route("/get_all_contacts", methods=['GET'])
def get_all_contacts():
    try:
        contacts = aleroDB.contacts.find()
        return jsonify({'contacts': [contact for contact in contacts]}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
