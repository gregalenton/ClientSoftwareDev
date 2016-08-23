from app import db
from app.models import User

# insert data
db.session.add(User("Bo Malicay", "NASA-lupa", "tester1", "testing", "+639324184369"))
db.session.add(User("Greg Alenton", "NASA-tubig", "tester2", "testing", "+639151092427"))

# commit the changes
db.session.commit()