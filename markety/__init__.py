from flask import Flask

from markety.models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite'

db.init_app(app)

import markety.models
import markety.views

with app.app_context():
    db.create_all()
