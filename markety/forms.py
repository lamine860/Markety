from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    name = StringField('name', validators=[
                       DataRequired(), Length(min=5, max=50)])
    email = StringField('email', validators=[Email()])
    password = StringField('password', validators=[
                           DataRequired(), Length(min=6, max=120), EqualTo('password_confirm')])
    password_confirm = StringField(
        'password_Confirm', validators=[DataRequired(), ])


class LoginForm(FlaskForm):
    email = StringField('email', validators=[Email()])
    password = StringField('password', validators=[DataRequired()])
