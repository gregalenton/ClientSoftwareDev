from app import db
from app.models import User

# insert data
db.session.add(User("Bo Malicay", "NASA-lupa", "bomalicay", "secret"))
db.session.add(User("Greg Alenton", "NASA-tubig", "gregalen", "baso"))

# commit the changes
db.session.commit()