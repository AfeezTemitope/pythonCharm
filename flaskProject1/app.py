from flask import Flask

app = Flask(__name__)


@app.route('/hello/<string:name>', methods=['GET'])
def hello_world(name):
    return f'Hello {name}'


if __name__ == '__main__':
    app.run()
