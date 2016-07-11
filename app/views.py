from flask import render_template, redirect, url_for, g
from flask_login import login_required, current_user
from app import app
from .forms import LoginForm

@app.route('/')
def index():
	g.db = connect_db()
	cur = g.db.execute('select * from posts')
	posts = [dict(title=row[], description=row[1]) for row in cur.fetchall()]
	g.db.close()
	return render_template('index.html')

@app.route('/login')
def login():
	form = LoginForm()
	return render_template('login.html', 
							form=form)