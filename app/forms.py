from flask_wtf import Form
from wtforms import *
from wtforms.validators import *

class LoginForm(Form):
	username = StringField('Username', validators[DataRequired()])
	password = PasswordField('Password', validators[DataRequired()])