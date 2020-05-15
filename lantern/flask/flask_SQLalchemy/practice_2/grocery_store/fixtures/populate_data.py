import csv
<<<<<<< HEAD
import os

from grocery_store import app, db
from grocery_store.models import User, Good
from grocery_store.config import FIXTURES_DIR
from sqlalchemy_utils import create_database, drop_database, database_exists

USERS_DIR = os.path.join(FIXTURES_DIR, 'users.csv')
GOODS_DIR = os.path.join(FIXTURES_DIR, 'goods.csv')


def get_users():
    with open(USERS_DIR, 'r') as f:
        reader = csv.DictReader(f)
        users = [i for i in reader]
=======
import logging
import os

from grocery_store import app, db
from grocery_store.models import User, Good, Store
from grocery_store.config import FIXTURES_DIR, Config
from sqlalchemy_utils import create_database, drop_database, database_exists

USERS_DIR = os.path.join(FIXTURES_DIR, "users.csv")
GOODS_DIR = os.path.join(FIXTURES_DIR, "goods.csv")
STORES_DIR = os.path.join(FIXTURES_DIR, "stores.csv")
logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)-6s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        # filename="logfile.log",  # if you want!!!
    )


def get_users():
    with open(USERS_DIR, "r") as f:
        reader = csv.DictReader(f)
        users = [user for user in reader]
>>>>>>> 07722339c99dd33be2e3cb7e7e17979304143f23
    return users


def get_goods():
<<<<<<< HEAD
    with open(GOODS_DIR, 'r') as f:
        reader = csv.DictReader(f)
        goods = [i for i in reader]
    return goods


with app.app_context():
    if database_exists(db.engine.url):
        db.create_all()
        print('Database exists')
    else:
        print(f"Database does not exists {db.engine.url}")
        create_database(db.engine.url)
        print('Data base created')
=======
    with open(GOODS_DIR, "r") as f:
        reader = csv.DictReader(f)
        goods = [good for good in reader]
    return goods


def get_stores():
    with open(STORES_DIR, "r") as f:
        reader = csv.DictReader(f)
        stores = [store for store in reader]
    return stores


with app.app_context():
    if not database_exists(db.engine.url):
        logging.info(f'Database "{Config.DB_NAME}" does not exists')
        create_database(db.engine.url)
        logging.info(f'Creating database "{Config.DB_NAME}"...')
        logging.info("Database successfully created")
    db.create_all()
    logging.info(f'Database "{Config.DB_NAME}" exists')
    logging.info("Connection to database...")
    logging.info("Connection succeeded!")
>>>>>>> 07722339c99dd33be2e3cb7e7e17979304143f23

with app.app_context():
    users = get_users()
    goods = get_goods()
<<<<<<< HEAD
=======
    stores = get_stores()
>>>>>>> 07722339c99dd33be2e3cb7e7e17979304143f23
    for user in users:
        db.session.add(User(**user))
    for good in goods:
        db.session.add(Good(**good))
<<<<<<< HEAD
    db.session.commit()
    print('Data written in data_base succesfuly')
=======
    for store in stores:
        db.session.add(Store(**store))
    db.session.commit()
    logging.info("Data added to database successfully")
>>>>>>> 07722339c99dd33be2e3cb7e7e17979304143f23