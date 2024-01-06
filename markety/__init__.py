from flask import Flask
from flask_login import LoginManager
from markety.models import User

from markety.auth import auth
from markety.product import product
from markety.database import db_session


app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'

app.register_blueprint(auth)
app.register_blueprint(product)
app.config['SECRET_KEY'] = '75e808bf48f40ed3a80bbde3f5b4b44d7bd5095bf1fc46a47bb1ac79fc5008d1'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
