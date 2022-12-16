from flask_wtf import *
from wtforms import *
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.auth.models import User


def email_check(form, field):
    if email := User.query.filter_by(user_email=field.data).first():
        raise ValidationError('That email already exists in our system.')


class RegistrationForm(FlaskForm):
    name = StringField('Enter you name', validators=[DataRequired(), Length(3, 15, message='Please enter a name between 3 and 15 characters.')])
    email = StringField('Enter you email', validators=[DataRequired(), Email(), email_check])
    password = PasswordField('Password', validators=[DataRequired(), Length(5, 12), EqualTo('confirm', message='Passwords are not equal')])
    confirm = PasswordField('Confirm password', validators=[DataRequired()])
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    stay_loggedin = BooleanField('Stay logged-in')
    submit = SubmitField('LogIn')