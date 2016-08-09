from app import db
from app.models import User

# insert data
db.session.add(User("Bo Malicay", "NASA-lupa", "tester1", "testing"))
db.session.add(User("Greg Alenton", "NASA-tubig", "tester2", "testing"))

# commit the changes
db.session.commit()