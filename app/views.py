from flask import redirect, render_template, request, url_for, jsonify, request
from flask_login import current_user, login_user, login_required, logout_user
from app import app
from functools import wraps
from .forms import LoginForm, SupportTicketForm
from sql import c
from passlib.hash import sha256_crypt
from .models import User
import gc

# twilio
import twilio.twiml
from twilio.util import TwilioCapability

@app.route('/index')
@login_required
def index():
	c.execute('SELECT * FROM leads WHERE clientID=?', (current_user.id,))
	entries = [dict(id=row[0],
					name=row[2],
					phoneNumber=row[3], 
					email=row[4],
					inquiry=row[5]) for row in c.fetchall()]
	return render_template('index.html', entries=entries)

@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
	logout()
	error = None
	form = LoginForm()
	if request.method == 'POST':
		if form.validate_on_submit():
			user = User.query.filter_by(username=request.form['username']).first()
			if user is not None and sha256_crypt.verify(request.form['password'], user.password):
				login_user(user)
				return redirect(url_for('index'))
			else:
				error = 'Invalid username or password.'
	return render_template('login.html', form=form, error=error)

@app.route('/logout')
@login_required
def logout():
	logout_user()
	form = LoginForm()
	return render_template('login.html', form=form)

@app.route('/leads')
def leads():
	c.execute('SELECT * FROM leads WHERE clientID=1')
	entries = [dict(id=row[0],
					name=row[2],
					phoneNumber=row[3],
					email=row[4],
					inquiry=row[5]) for row in c.fetchall()]
	return render_template('leads.html', entries=entries)

@app.route('/calls')
def calls():

	return render_template('calls.html')

@app.route('/mail')
def mail():
	return render_template('mail.html')

@app.route('/voice', methods=['GET', 'POST'])
def voice():
	dest_number = request.values.get('PhoneNumber', None)

	resp = twilio.twiml.Response()

	with resp.dial(callerId=caller_id) as r:
		if dest_number and re.search('^[\d\(\)\- \+]+$', dest_number):
			r.number(dest_number)
		else:
			r.client(dest_number)

	return str(resp)

@app.route('/client', methods=['GET', 'POST'])
def client():
	"""Respond to incoming requests."""

	client_name = request.values.get('client', None) or "jenny"

	capability = TwilioCapability('TWILIO_ACCOUNT_SID', 'TWILIO_AUTH_TOKEN')
	capability.allow_client_outgoing('TWILIO_APP_SID')
	token = capability.generate()

	return render_template('client.html', token=token)