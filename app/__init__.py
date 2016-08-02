#imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os
import sqlite3

#create application
app = Flask(__name__, instance_relative_config=True)
<<<<<<< HEAD
app.database = "tmp/sample.db"
=======
#app.database = "tmp/sample.db"

>>>>>>> 603e32d8c9a1b7fdbcac20b2b54aa8166731c66f

#configurations
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
app.config.from_envvar('APP_SETTINGS', silent=True)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config.from_pyfile('config.py')

from app import views
from models import User
from db_create import *
from db_create_users import *

login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
	return User.query.filter(User.id == int(user_id)).first()