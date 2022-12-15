from flask_wtf import *
from wtforms import *

class RegistrationForm(FlaskForm):
    name = StringField('Enter you name')
    email = StringField('Enter you email')
    submit = SubmitField('Register')

