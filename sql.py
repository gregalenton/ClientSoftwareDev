import sqlite3
from passlib.hash import sha256_crypt

with sqlite3.connect("sample.db", check_same_thread=False) as connection:
	c = connection.cursor()
	
# def createTables():
# 	#drop existing tables if exists
# 	# c.execute("DROP TABLE clients")
# 	# c.execute("DROP TABLE leads")

# 	#create clients table
# 	c.execute('''CREATE TABLE clients
#  			(id INTEGER PRIMARY KEY,
#  			clientName TEXT NOT NULL,
#  			clientCompany TEXT NOT NULL,
#  			username TEXT NOT NULL,
#  			password TEXT NOT NULL
#  			)''')

# 	#create leads table
# 	c.execute('''CREATE TABLE leads
# 	 		(leadID INTEGER PRIMARY KEY,
# 	 		owner TEXT NOT NULL,
# 	 		leadName TEXT NOT NULL,
# 	 		leadPhoneNumber TEXT,
# 	 		leadEmail TEXT,
# 	 		leadInquiry TEXT,
# 	 		FOREIGN KEY(owner) REFERENCES clients(id)
# 			)''')

# def addClient(clientName, clientCompany, username, password):
# 	c.execute('''INSERT INTO clients (clientName, clientCompany, username, password)
# 	VALUES (?,?,?,?)''',(clientName, clientCompany, username, password))

# def addLead(owner, leadName, leadPhoneNumber, leadEmail, leadInquiry):
# 	c.execute('''INSERT INTO leads (owner, leadName, leadPhoneNumber, leadEmail, leadInquiry)
# 	VALUES (?,?,?,?,?)''',(owner, leadName, leadPhoneNumber, leadEmail, leadInquiry))

	#drop tables
	c.execute("DROP TABLE clients")
	c.execute("DROP TABLE leads")
	
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
			(leadID INTEGER PRIMARY KEY,
			owner TEXT NOT NULL,
			leadName TEXT NOT NULL,
			leadPhoneNumber TEXT,
			leadEmail TEXT,
			leadInquiry TEXT,
			FOREIGN KEY(owner) REFERENCES clients(id)
			)''')
	
	#dummy data
	#hash password for dummy data
	hashed = sha256_crypt.encrypt("secret")
	c.execute('INSERT INTO clients VALUES("0001", "Bo Malicay", "Jollibo", "bomalicay", ?)', (hashed, ))
	c.execute('INSERT INTO leads VALUES("0001", "0001", "LEADer", "09324184369", "mslmalicay@gmail.com", "Pano po ba magmove on?")')