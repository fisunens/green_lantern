from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from grocery_store.config import Config
<<<<<<< HEAD
from grocery_store.routes import users, goods
=======
from grocery_store.routes import users, goods, stores
>>>>>>> 07722339c99dd33be2e3cb7e7e17979304143f23
from grocery_store.db import db


def make_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(users)
    app.register_blueprint(goods)
<<<<<<< HEAD
    return app

=======
    app.register_blueprint(stores)
    return app


>>>>>>> 07722339c99dd33be2e3cb7e7e17979304143f23
def make_db(app):
    db.init_app(app)
    return db