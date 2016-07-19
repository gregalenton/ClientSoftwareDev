from flask import render_template, redirect, url_for
from flask_login import login_required, current_user
from app import app
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	return render_template('login.html', 
							form=form)

@app.route('/leads')
def leads():
	return render_template('leads.html')

@app.route('/calls')
def calls():
	return render_template('calls.html')

@app.route('/mail')
def mail():
	return render_template('mail.html')