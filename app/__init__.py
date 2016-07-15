#imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
#from sql import createTables, addClient, addLead
import os
import bcrypt


#create application
app = Flask(__name__, instance_relative_config=True)

#configurations
db = SQLAlchemy(app)
#bcrypt = Bcrypt(app)
app.config.from_envvar('APP_SETTINGS', silent=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')

#app.database = "sample.db"
#createTables()
#create dummy client
#hash password for dummy data
# hashed = bcrypt.hashpw('secret', bcrypt.gensalt(10))
# addClient('Bo Malicay', 'Jollibo', 'bomalicay', hashed)
# addLead('Bo Malicay', 'name of lead', '09324184369', 'mslmalicay@gmail.com', 'How to be you po')

from app import views
#from app import models