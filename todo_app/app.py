from flask import Flask

from models import db
from urls import bp

app = Flask(__name__)
app.config.from_object('config.Config')

app.register_blueprint(bp)
db.init_app(app)


with app.app_context():
    db.create_all()


if __name__ == '__main__':
    app.run()
