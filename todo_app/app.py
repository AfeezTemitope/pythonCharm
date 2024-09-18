from flask import Flask
from flask_jwt_extended import JWTManager
from models import db
from urls import todo_bp

app = Flask(__name__)
app.config.from_object('config.Config')

jwt = JWTManager(app)
app.register_blueprint(todo_bp)

db.init_app(app)


with app.app_context():
    db.create_all()


if __name__ == '__main__':
    app.run()
