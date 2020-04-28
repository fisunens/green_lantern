from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import create_database, drop_database, database_exists
from config import Config
from populate_data import get_users, get_goods, get_stores

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), unique=True, nullable=False)
    email = db.Column(db.String(), unique=True, nullable=False)
    password = db.Column(db.String(), unique=True, nullable=False)


class Good(db.Model):
    __tablename__ = "goods"

    good_id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(), unique=False, nullable=False)
    name = db.Column(db.String(), unique=True, nullable=False)
    price = db.Column(db.Float, nullable=False)


class Store(db.Model):
    __tablename__ = "stores"

    store_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), unique=True, nullable=False)
    city = db.Column(db.String(), unique=False, nullable=False)
    address = db.Column(db.Unicode(), unique=False, nullable=False)
    manager_id = db.Column(db.Integer, nullable=False)


app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    if database_exists(db.engine.url):
        db.create_all()
        print('database exists')
    else:
        print(f'database does not exists {db.engine.url}')
        create_database(db.engine.url)
        print('database created')

with app.app_context():
    users = get_users()
    for user in users:
        db.session.add(User(**user))
    db.session.commit()
    print('Users written in data_base successfully')

with app.app_context():
    goods = get_goods()
    for good in goods:
        db.session.add(Good(**good))
    db.session.commit()
    print('Goods written in data_base successfully')

with app.app_context():
    stores = get_stores()
    for store in stores:
        db.session.add(Store(**store))
    db.session.commit()
    print('Stores written in data_base successfully')
