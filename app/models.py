from app import db
from flask_user import UserMixin, UserManager, SQLAlchemyAdapter


#lead class
class Lead(db.Model):

	__tablename__ = "leads"

	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	clientID = db.Column(db.Integer)
	leadName = db.Column(db.String, nullable=False)
	leadPhoneNumber = db.Column(db.String)
	leadEmail = db.Column(db.String)
	leadInquiry = db.Column(db.String)

	def __init__(self, clientID, leadName, leadPhoneNumber, leadEmail, leadInquiry):
		self.clientID = clientID
		self.leadName = leadName
		self.leadPhoneNumber = leadPhoneNumber
		self.leadEmail = leadEmail
		self.leadInquiry = leadInquiry
		
	def __repr__(self):
		return '<leadName {}'.format(self.leadName)


#client class
class Client(db.Model, UserMixin):

	__tablename__ = "clients"

	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	clientName = db.Column(db.String, nullable=False)
	clientCompany = db.Column(db.String, nullable=False)
	username = db.Column(db.String, nullable=False)
	password = db.Column(db.String, nullable=False)

	def __init__(self, clientName, clientCompany, username):
   		self.clientName = clientName
    	self.clientCompany = clientCompany
    	self.username = username

	def is_authenticated(self):
		return True

	def is_active(self):
		return True

	def is_anonymous(self):
		return False

	def get_id(self):
		return unicode(self.id)

	def __repr__(self):
		return '<leadName - {}'.format(self.leadName)