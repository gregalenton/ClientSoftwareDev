from app import db

#create the database and the db table
db.create_all()

#insert data
#db.session.add(BlogPost("Good", "I\'m good."))
#db.session.add(BlogPost("Well", "I\'m well."))

#commit changes
db.session.commit()