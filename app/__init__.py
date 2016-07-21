#imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os
import bcrypt
import sqlite3

#create application
app = Flask(__name__, instance_relative_config=True)
app.database = "tmp/sample.db"

#configurations
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
app.config.from_envvar('APP_SETTINGS', silent=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')

from app import views
from models import User
from db_create_users import *

login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
	return User.query.filter(User.id == int(user_id)).first()