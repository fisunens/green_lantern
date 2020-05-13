from grocery_store.app import make_app, make_db, make_manager
<<<<<<< HEAD
from flask_script import Server, Manager
=======
>>>>>>> 6f0c3857e9ca686bf53e9ceb682f2a2afbfbaa8f
from grocery_store.config import Config

app = make_app()
db = make_db(app)
manager = make_manager(app)
<<<<<<< HEAD
=======

>>>>>>> 6f0c3857e9ca686bf53e9ceb682f2a2afbfbaa8f

__all__ = ["app", "db", "manager"]
