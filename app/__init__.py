#imports
import os
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
import sqlite3

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

#create sqlalchemy object
db = SQLAlchemy(app)

def connect_db():
	"""Connects to the specific database."""
	rv = sqlite3.connect(app.config['DATABASE'])
	rv.row_factory = sqlite3.Row
	return rv