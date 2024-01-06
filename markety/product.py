import functools
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from markety.database import db_session
from flask_login import login_required

product = Blueprint('products', __name__)


@product.route('/')
def home():
    return render_template('home.html')
