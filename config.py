import os

#default config
class BaseConfig(object):
	DEBUG = True
	SECRET_KEY = '\x0bj-0\xe7\x1eY\x86\xb1\x02D\x9dnZ/\xd7d\xb6!\x11%i\xde\xb1'
	SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
	WTF_CSRF_ENABLED = True
	SQLALCHEMY_TRACK_MODIFICATIONS = True


class DevelopmentConfig(BaseConfig):
	DEBUG = True
	
class ProductionConfig(BaseConfig):
	DEBUG = False