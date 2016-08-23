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
from twilio.rest import TwilioRestClient
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
	c.execute('SELECT * FROM leads WHERE clientID=?', (current_user.id,))
	entries = [dict(id=row[0],
					name=row[2],
					phoneNumber=row[3],
					email=row[4],
					inquiry=row[5]) for row in c.fetchall()]
	return render_template('leads.html', entries=entries)

@app.route('/calls', methods=['GET', 'POST'])
def calls():
	
	return render_template('calls.html')

@app.route('/mail')
def mail():
	
	return render_template('mail.html')

@app.route('/calls', methods=['POST'])
def call():
	# # Return TwiML instructions to Twilio's POST requests
	# response = twiml.Response()

	# with response.dial(callerId=app.config['TWILIO_CALLER_ID']) as dial:
	# # 	# if the browser sent a phonenumber param, the request is a user trying to call a customer's phone
	# # 	# if 'phoneNumber' in request.form:
	# # 	# 	dial.number(request.form['phoneNumber'])
	# 	if True:
	# 		dial.number('+639324184369')
	# 	else:
	# 		# Otherwise it is a customer trying to contact the user 
	# 		dial.client('support_agent')

	# return str(response)

	#basic
	client = TwilioRestClient(app.config['TWILIO_ACCOUNT_SID'], app.config['TWILIO_AUTH_TOKEN'])
	call = client.calls.create(to="+639324184369", from_=current_user.user_phonenumber, url="https://leadfunnel-sales-wizard.herokuapp.com/calls")

	return call.sid