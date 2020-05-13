from grocery_store.db import db


class User(db.Model):
    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), nullable=False)
    password = db.Column(db.String(), nullable=False)

    def __repr__(self):
<<<<<<< HEAD
        return f'<id: {self.user_id}, name: {self.name}, email: {self.email}>'
=======
        return f"<id: {self.user_id}, name: {self.name}, email: {self.email}>"
>>>>>>> 07722339c99dd33be2e3cb7e7e17979304143f23


class Good(db.Model):
    __tablename__ = "goods"

    good_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    brand = db.Column(db.String(), nullable=False)
<<<<<<< HEAD
    price = db.Column(db.Integer(), nullable=False)
=======
    price = db.Column(db.Integer, nullable=False)


class Store(db.Model):
    __tablename__ = "stores"

    store_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    city = db.Column(db.String(), nullable=False)
    address = db.Column(db.String(), nullable=False)
    manager_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)
>>>>>>> 07722339c99dd33be2e3cb7e7e17979304143f23
