from flask import redirect, render_template, request, url_for, jsonify, request
from flask_login import current_user, login_user, login_required, logout_user
from app import app
from functools import wraps
from .forms import LoginForm, SupportTicketForm
from sql import c
from flask import jsonify
from passlib.hash import sha256_crypt
from .models import User
import gc

# twilio
from twilio import twiml
from twilio.util import TwilioCapability

def get_token():
	# Return a twilio Client token
	capability = TwilioCapability(
		app.config['TWILIO_ACCOUNT_SID'],
		app.config['TWILIO_AUTH_TOKEN'])

	#allow users to make outgoing calls with twilio client
	capability.allow_client_outgoing(app.config['TWIML_APPLICATION_SID'])

	token = capability.generate()

	return jsonify({'token': token})


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
	c.execute('SELECT * FROM leads WHERE clientID=?', (current_user.id,))
	entries = [dict(id=row[0],
					name=row[2],
					phoneNumber=row[3],
					email=row[4],
					inquiry=row[5]) for row in c.fetchall()]
	return render_template('leads.html', entries=entries)

@app.route('/calls')
def calls():
	call()
	return render_template('calls.html')

@app.route('/mail')
def mail():
	
	return render_template('mail.html')


def call():
	# Return TwiML instructions to Twilio's POST requests
	response = twiml.Response()

	with response.dial(callerId=app.config['TWILIO_CALLER_ID']) as dial:
		# if the browser sent a phonenumber param, the request is a user trying to call a customer's phone
		# if 'phoneNumber' in request.form:
		# 	dial.number(request.form['phoneNumber'])
		if True:
			dial.number('+639151092427')
		else:
			# Otherwise it is a customer trying to contact the user 
			dial.client('support_agent')

	return str(response)
