from flask_restful import fields

users_structure = {
    "user_id": fields.Integer,
    "name": fields.String,
    "email": fields.String,
}

goods_structure = {
<<<<<<< HEAD
    'good_id': fields.Integer,
    'name': fields.String,
    'brand': fields.String,
=======
    "good_id": fields.Integer,
    "name": fields.String,
    "brand": fields.String,
    "price": fields.Integer,
}
stores_structure = {
    "store_id": fields.Integer,
    "name": fields.String,
    "city": fields.String,
    "address": fields.String,
    "manager_id": fields.Integer,
>>>>>>> 07722339c99dd33be2e3cb7e7e17979304143f23
}
