from app import db

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

#lead class
class Lead(db.Model):

	__tablename__ = "leads"

	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	leadName = db.Column(db.String, nullable=False)
	leadPhoneNumber = db.Column(db.String)
	leadEmail = db.Column(db.String)
	leadInquiry = db.Column(db.String)
	userID = db.Column(db.Integer, ForeignKey('users.id'))

	def __init__(self, userID, leadName, leadPhoneNumber, leadEmail, leadInquiry):
		self.userID = userID
		self.leadName = leadName
		self.leadPhoneNumber = leadPhoneNumber
		self.leadEmail = leadEmail
		self.leadInquiry = leadInquiry
		
	def __repr__(self):
		return '<leadName {}'.format(self.leadName)


#client class
class User(db.Model):

	__tablename__ = "users"

	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	user_Name = db.Column(db.String, nullable=False)
	user_Company = db.Column(db.String, nullable=False)
	username = db.Column(db.String, nullable=False)
	password = db.Column(db.String, nullable=False)
	leads = relationship("Lead", backref="owner")

	def __init__(self, user_Name, user_Company, username):
		self.user_Name = cuser_Name
		self.user_Company = user_Company
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
		return '<user_Name - {}'.format(self.user_Name)