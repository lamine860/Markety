from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from markety.models import User
from markety.forms import RegistrationForm, LoginForm
from markety.database import db_session

from flask_login import login_user, logout_user

auth = Blueprint('auth', __name__, url_prefix='/auth')


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate_on_submit():
        data = form.data
        if User.query.filter_by(name=data['name']).first():
            form.name.errors.append('Name already taken!')
        elif User.query.filter_by(email=data['email']).first():
            form.email.errors.append('Email already taken!')
        else:
            user = User(data['name'], data['email'],
                        generate_password_hash(data['password']))
            db_session.add(user)
            db_session.commit()
            flash('Registration success!')
            return redirect(url_for('auth.login'))

    return render_template('auth/register.html', form=form)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        user = User.query.filter_by(email=form.data['email']).first()
        if user is not None and check_password_hash(user.password, form.data['password']):
            db_session.add(user)
            db_session.commit()
            login_user(user)
            return redirect(url_for('products.home'))
        else:
            form.email.errors.append('No account found with this credentials')

    return render_template('auth/login.html', form=form)


@auth.route('/logout', methods=['POST'])
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
