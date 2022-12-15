from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
import unittest

class LoginForm(FlaskForm):
    username = StringField('UserName', validators=[DataRequired()] )
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Send') 