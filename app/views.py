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
import twilio.twiml
from twilio.util import TwilioCapability
from twilio.rest import TwilioRestClient

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
	call()
	return render_template('calls.html')

@app.route('/mail')
def mail():
	
	return render_template('mail.html')

# @app.route('/calls', methods=['POST'])
def call():
	# Get phone number we need to call
	phone_number = "+639324184369"

	try:
		twilio_client = TwilioRestClient(app.config['TWILIO_ACCOUNT_SID'],
										app.config['TWILIO_AUTH_TOKEN'])
	except Exception as e:
		msg = "Missing configuration variable: {0}".format(e)
		return jsonify({'error': msg})

	try:
		twilio_client.calls.create(from_=app.config['TWILIO_CALLER_ID'],
									to=phone_number,
									url=url_for('calls',
												_external=True))

	except Exception as e:
		app.logger.error(e)
		return jsonify({'message': 'Call incoming!'})

@app.route('/outbound', methods=['POST'])
def outbound():
	response = twiml.Response()

	response.say("Hello there. It's me Bo, from Leadfunnel.ph", voice='alice')

	with response.dial() as dial:
		dial.number("+639324184369")

	return str(response)