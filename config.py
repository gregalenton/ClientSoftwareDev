import os

#default config
class BaseConfig(object):
	DEBUG = True
	SECRET_KEY = '\x0bj-0\xe7\x1eY\x86\xb1\x02D\x9dnZ/\xd7d\xb6!\x11%i\xde\xb1'
	SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
	WTF_CSRF_ENABLED = True
	SQLALCHEMY_TRACK_MODIFICATIONS = True
	#Twilio
	TWILIO_ACCOUNT_SID = 'ACf49e7e3210b0d62e18d0896c43faec2d'
	TWILIO_AUTH_TOKEN = 'cda8d559b05c77535967c816ce076b2c'
	TWILIO_CALLER_ID = "+639177216516"
	TWILIO_APPLICATION_SID = "AP2f8a4ffab3a95521b2c64f27e8772916"
	TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID', None)
	TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN', None)
	TWILIO_CALLER_ID = os.environ.get('TWILIO_CALLER_ID', None)
	TWILIO_APPLICATION_SID = os.environ.get('TWILIO_APPLICATION_SID', None)


class DevelopmentConfig(BaseConfig):
	DEBUG = True
	
class ProductionConfig(BaseConfig):
	DEBUG = False