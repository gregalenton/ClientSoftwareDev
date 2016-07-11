import sqlite3

with sqlite3.connect("sample.db") as connection:
	c = connection.cursor()
	c.execute("DROP TABLE clients")
	c.execute("DROP TABLE leads")
	
	#create clients table
	c.execute('''CREATE TABLE clients
				(clientID INT NOT NULL, 
				clientName TEXT NOT NULL,
				clientCompany TEXT NOT NULL,
				clientUserName TEXT NOT NULL,
				clientPassword TEXT NOT NULL,
				PRIMARY KEY(clientID)
				)''')

	#create leads table
	c.execute('''CREATE TABLE leads
				(clientID INT NOT NULL,
				leadID INT NOT NULL,
				leadName TEXT NOT NULL,
				leadPhoneNumber TEXT,
				leadEmail TEXT,
				leadInquiry TEXT,
				FOREIGN KEY(clientID) REFERENCES clients(clientID)
				)''')
	
	c.execute('INSERT INTO clients VALUES("0001", "Bo Malicay", "Jollibo", "bomalicay", "lollipop2015")')
	c.execute('INSERT INTO leads VALUES("0001", "0001", "LEADer", "09324184369", "mslmalicay@gmail.com", "Pano po ba magmove on?")')