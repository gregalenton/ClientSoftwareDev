from . import db
from flask.ext.user import UserMixin, UserManager, SQLAlchemyAdapter

class User(db.Model, UserMixin):

	id = db.Column('user_id', db.Integer, primary_key = True, autoincrement = True)
	username = db.Column('username', db.String(50), nullable=False, unique=True)
	password = db.Column('password', db.String(255), nullable=False, server_default='')