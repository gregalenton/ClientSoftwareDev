from flask import *
from flask_login import *
from .forms import * 


@app.route('/')
@login_required
def index():
	return render_template("")

@app.route('/login')
def login():
	form = LoginForm()
	
	return render_template("")