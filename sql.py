import sqlite3
from passlib.hash import sha256_crypt

with sqlite3.connect("sample.db", check_same_thread=False) as connection:
	c = connection.cursor()
	
# def createTables():
#drop existing tables if exists
c.execute('DROP TABLE IF EXISTS leads')
#create users table
# c.execute('''CREATE TABLE users
# 		(id INTEGER PRIMARY KEY,
# 		user_Name TEXT NOT NULL,
# 		user_Company TEXT NOT NULL,
# 		username TEXT NOT NULL,
# 		password TEXT NOT NULL
# 		)''')
#create leads table
c.execute('''CREATE TABLE leads
 		(id INTEGER PRIMARY KEY,
 		clientID TEXT NOT NULL,
 		leadName TEXT NOT NULL,
 		leadPhoneNumber TEXT,
 		leadEmail TEXT,
 		leadInquiry TEXT,
 		call_status TEXT, 
 		email_status TEXT
		)''')
		# call_status (dialled, missed, received)
		# email_status (read, unread)

# def addClient(clientName, clientCompany, username, password):
# 	c.execute('''INSERT INTO clients (clientName, clientCompany, username, password)
# 				VALUES (?,?,?,?)''',(clientName, clientCompany, username, password))

def addLead(clientID, leadName, leadPhoneNumber, leadEmail, leadInquiry):
	c.execute('''INSERT INTO leads (clientID, leadName, leadPhoneNumber, leadEmail, leadInquiry)
				VALUES (?,?,?,?,?)''',(clientID, leadName, leadPhoneNumber, leadEmail, leadInquiry))

#dummy data
#addClient('Bo Malicay', 'NASA-lupa', 'bomalicay', sha256_crypt.encrypt("secret"))	
addLead('1', 'Juan dela Cruz', '09324284362', 'juandelacruz@gmail.com', 'How much is the 2 bedroom condo? What are the payment terms?')
addLead('1', 'John Smith', '09425346787', 'john.smith@hotmail.com', 'I\'m very much interested with the 1 bedroom condo with balcony. Is Pag-Ibig applicable with this?')
addLead('2', 'Alice Green', '09324567890', 'agreen@gmail.com', 'When is the turnover? What are the payment terms? The downpayment?')
addLead('2', 'Marco Buttondown', '09321112233', 'marcobuttons@hotmail.com', 'Do you do in-house financing? Would like to invest in 3-bedroom condo.')
addLead('2', 'Clark Santos', '09324445567', 'CSantos@yahoo.com', 'How do I invest? What are the requirements?')
addLead('1', 'Juan dela Cruz', '09324284362', 'juandelacruz@gmail.com', 'How much is the 2 bedroom condo? What are the payment terms?')
addLead('1', 'John Smith', '09425346787', 'john.smith@hotmail.com', 'I am very much interested with the 1 bedroom condo with balcony. Is Pag-Ibig applicable with this?')
addLead('1', 'Alice Green', '09324567890', 'aliceg@gmail.com', 'When is the turnover? What are the payment terms? The downpayment?')
addLead('1', 'Marco Buttondown', '09321112233', 'marcobuttons@hotmail.com', 'Do you do in-house financing? Would like to invest in 3-bedroom condo.')
addLead('1', 'Jessica Bell', '09324445567', 'jessbell@yahoo.com', 'How do I invest? What are the requirements?')
connection.commit()
#connection.close()