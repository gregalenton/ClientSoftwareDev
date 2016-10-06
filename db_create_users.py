from app import db
from app.models import User

# insert data
db.session.add(User("Bo Malicay", "NASA-lupa", "admin", "admin", "+639151092427"))
db.session.add(User("Greg Alenton", "NASA-tubig", "admin2", "admin2", "+639151092427"))

# commit the changes
db.session.commit()