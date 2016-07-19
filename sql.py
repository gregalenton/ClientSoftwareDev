import sqlite3
from passlib.hash import sha256_crypt

with sqlite3.connect("tmp/sample.db", check_same_thread=False) as connection:
	c = connection.cursor()
	
# def createTables():
#drop existing tables if exists
c.execute('DROP TABLE IF EXISTS clients')
c.execute('DROP TABLE IF EXISTS leads')
	#create clients table
c.execute('''CREATE TABLE clients
		(id INTEGER PRIMARY KEY,
		clientName TEXT NOT NULL,
		clientCompany TEXT NOT NULL,
		username TEXT NOT NULL,
		password TEXT NOT NULL
		)''')
#create leads table
c.execute('''CREATE TABLE leads
 		(id INTEGER PRIMARY KEY,
 		clientID TEXT NOT NULL,
 		leadName TEXT NOT NULL,
 		leadPhoneNumber TEXT,
 		leadEmail TEXT,
 		leadInquiry TEXT,
 		FOREIGN KEY(clientID) REFERENCES clients(id)
		)''')

def addClient(clientName, clientCompany, username, password):
	c.execute('''INSERT INTO clients (clientName, clientCompany, username, password)
				VALUES (?,?,?,?)''',(clientName, clientCompany, username, password))

def addLead(clientID, leadName, leadPhoneNumber, leadEmail, leadInquiry):
	c.execute('''INSERT INTO leads (clientID, leadName, leadPhoneNumber, leadEmail, leadInquiry)
				VALUES (?,?,?,?,?)''',(clientID, leadName, leadPhoneNumber, leadEmail, leadInquiry))

#dummy data
# createTables()
addClient('Bo Malicay', 'Jollibo', 'bomalicay', sha256_crypt.encrypt("secret"))	
addLead('1', 'lead_name', '09324184369', 'mslmalicay@gmail.com', 'How to be you po?')
connection.commit()
#connection.close()