from datetime import timedelta

from auth import auth
from config import run_config
from create_db import create_db
from db import db
from flask import Flask
from many_to_many_example import many_to_many
from news import news
from one_to_many_example import one_to_many


def run_app():
    app = Flask(__name__)
    app.config.from_object(run_config())

    db.init_app(app)
    app.permanent_session_lifetime = timedelta(minutes=20)  # add session expire time

    app.register_blueprint(auth)
    app.register_blueprint(create_db)
    app.register_blueprint(news)
    app.register_blueprint(one_to_many)
    app.register_blueprint(many_to_many)

    return app
