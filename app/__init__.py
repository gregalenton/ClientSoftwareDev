<<<<<<< HEAD
#imports
import os
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
import sqlite3
=======
from flask import Flask

>>>>>>> 0e2df85e34b2212c2b09eb6d18b4596291726d50

#create application
app = Flask(__name__, instance_relative_config=True)
app.config.update(dict(
	DATABASE=os.path.join(app.root_path, 'users.db'),
	SECRET_KEY='development key',
	USERNAME='admin',
	PASSWORD='default'
))
app.config.from_envvar('CliLead_SETTINGS', silent=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')

app.database = "sample.db"

<<<<<<< HEAD
#create sqlalchemy object
db = SQLAlchemy(app)

def connect_db():
	return sqlite3.connect(app.database)
=======
from app import views 
>>>>>>> 0e2df85e34b2212c2b09eb6d18b4596291726d50
