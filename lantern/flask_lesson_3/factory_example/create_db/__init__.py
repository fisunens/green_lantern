from create_db.routes import CreateDB
from flask import Blueprint
from flask_restful import Api

create_db = Blueprint("create_db", __name__)
api_create_db = Api(create_db)

api_create_db.add_resource(CreateDB, "/create_db")
