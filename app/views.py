from flask import *
from flask_login import current_user
from app import app
from functools import wraps
from .forms import LoginForm
from sql import c
from passlib.hash import sha256_crypt
import gc

def login_required(test):
	@wraps(test)
	def wrap(*args, **kwargs):
		error = ''
		if 'logged_in' in session:
			return test(*args, **kwargs)
		else:
			error = 'You need to login first.'
			return redirect(url_for('login'))																																																			
	return wrap


@app.route('/')
@app.route('/index')
@login_required
def index():
	c.execute("SELECT leadName, leadPhoneNumber, leadEmail, leadInquiry FROM leads ORDER BY id DESC")
	entries = c.fetchall()
	return render_template('index.html', entries, entries)

@app.route('/login', methods=['GET', 'POST'])
def login():
	logout()
	error = ''
	form = LoginForm()
	try:
		if request.method == 'POST':
			#getting username and password
			passw = c.execute("SELECT * FROM clients WHERE username=?", (request.form['username'],))
			passw = c.fetchone()[4]					 
			#check password if it matches
			if sha256_crypt.verify(request.form['password'], passw) == True:
				#logged in
				session['logged_in'] = True
				session['username'] = request.form['username']
				return redirect(url_for('index'))
			else: #password does not match the username
				error = 'Username and Password do not match!'
				return render_template('login.html', form=form, error=error)

	except Exception as e: #username does not exist
		error = 'Invalid credentials.'
		return render_template('login.html', form=form, error=error)

	gc.collect()
	return render_template('login.html', form=form)

	

@app.route('/logout')
@login_required
def logout():
	session.pop('logged_in', None)
	return redirect (url_for('login'))
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
