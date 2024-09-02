from flask import Flask, render_template
from flask_migrate import Migrate

from models import db, init_db
import pymysql
from urls import bp
import os

app = Flask(__name__)
app.config.from_object('config.Config')
app.register_blueprint(bp)
db.init_app(app)
migrate = Migrate(app, db)


def create_database_if_not_exists():

    db_config = {
        'host': os.environ.get('DB_HOST', 'localhost'),
        'user': os.environ.get('DB_USER', 'root'),
        'password': os.environ.get('DB_PASSWORD', 't3m1t@p3'),
        'port': int(os.environ.get('DB_PORT', 3306))
    }
    try:
        conn = pymysql.connect(**db_config)
        with conn.cursor() as cursor:
            cursor.execute("CREATE DATABASE IF NOT EXISTS note_mgt;")
        conn.commit()
    except pymysql.Error as e:
        print(f"Error creating database: {e}")
    finally:
        conn.close()


with app.app_context():
    init_db(app)


if __name__ == '__main__':
    app.run(debug=True)