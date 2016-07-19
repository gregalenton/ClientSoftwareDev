#imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os
import bcrypt

#create application
app = Flask(__name__, instance_relative_config=True)

#configurations
db = SQLAlchemy(app)
app.config.from_envvar('APP_SETTINGS', silent=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')

#app.database = "sample.db"

from app import views
#from app import models