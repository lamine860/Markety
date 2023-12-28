from flask import render_template, redirect
from markety import app
from markety.models import db, User


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/register')
def register():
    return render_template('auth/register.html')


@app.route('/login')
def login():
    users = db.session.execute(db.select(User))
    print('========', users, '============')
    return render_template('auth/login.html')


@app.route('/logout', methods=['POST'])
def logout():
    return redirect('/home')
