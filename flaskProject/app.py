from flask import Flask, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)
jan = MongoClient('mongodb://localhost:27017')
oluwafemi = jan['big-boy']


@app.route('/add_contact', methods=['POST'])
def add_contact():
    data = request.get_json()
    phone_number = data.get('phone_number')
    first_name = data.get('first_name')
    last_name = data.get('last_name')

    if validate(phone_number):
        saved_number = oluwafemi.note.find_one({'phoneNumber': phone_number})
        if saved_number:
            return jsonify({'message': 'Contact Already Exists'}), 400
        else:
            new_contact = {'phoneNumber': phone_number, "firstName": first_name, "lastName": last_name}
            oluwafemi.note.insert_one(new_contact)
            return jsonify({'message': 'Contact Added Successfully'}), 201
    else:
        return jsonify({'message': 'Phone Number is Invalid'}), 400


def validate(number) -> bool:
    return len(number) == 11 and number.isdigit()


@app.route('/get_contact', methods=['GET'])
def get_contact():
    data = request.args  # Use request.args for GET method shogbo bby
    phone_number = data.get('phone_number')

    if validate(phone_number):
        existing_number = oluwafemi.note.find_one({'phoneNumber': phone_number})
        if existing_number:
            return jsonify({
                'phone_number': existing_number.get('phoneNumber'),
                'first_name': existing_number.get('firstName'),
                'last_name': existing_number.get('lastName')
            }), 200
        else:
            return jsonify({'message': 'Number Not Found'}), 400
    else:
        return jsonify({'message': 'Phone Number is Invalid'}), 400


@app.route('/delete_contact', methods=['DELETE'])
def remove_contact():
    data = request.get_json()
    phone_number = data.get('phone_number')

    if validate(phone_number):
        result = oluwafemi.note.delete_one({'phoneNumber': phone_number})
        if result.deleted_count > 0:
            return jsonify({'message': 'Removed Successfully'}), 200
        else:
            return jsonify({'message': 'Phone Number Not Found'}), 400
    else:
        return jsonify({'message': 'Phone Number is Invalid'}), 400


@app.route('/update_contact', methods=['PUT'])
def update_contact():
    data = request.get_json()
    phone_number = data.get('phone_number')
    first_name = data.get('first_name')
    last_name = data.get('last_name')

    if validate(phone_number):
        result = oluwafemi.note.update_one(
            {'phoneNumber': phone_number},
            {'$set': {'firstName': first_name, 'lastName': last_name}}
        )
        if result.matched_count > 0:
            return jsonify({'message': 'Contact Updated Successfully'}), 200
        else:
            return jsonify({'message': 'Contact Not Found'}), 400
    else:
        return jsonify({'message': 'Phone Number is Invalid'}), 400


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
