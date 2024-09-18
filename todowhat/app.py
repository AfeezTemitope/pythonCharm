from flask import Flask, jsonify
from flask_jwt_extended import JWTManager
from models import db, BLOCKLIST
from urls import todo_bp

app = Flask(__name__)
app.config.from_object('config.Config')

jwt = JWTManager(app)
@jwt.token_in_blocklist_loader
def check_if_token_in_blocklist(jwt_header, jwt_payload):
    jti = jwt_payload['jti']
    return jti in BLOCKLIST


@jwt.revoked_token_loader
def revoked_token_callback(jwt_header, jwt_payload):
    return jsonify({"msg": "The token has been revoked"}), 401
app.register_blueprint(todo_bp)

db.init_app(app)


with app.app_context():
    db.create_all()


if __name__ == '__main__':
    app.run()
