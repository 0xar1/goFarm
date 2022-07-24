from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField, SubmitField, validators
from wtforms.validators import Email, InputRequired, Length, EqualTo


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    password = PasswordField('Password', validators=[InputRequired(),  Length(min=6,max=50)])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegisterForm(FlaskForm):   
    fullname = StringField('Username',validators=[InputRequired(), Length(max=50)]) 
    email = StringField('Email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    password = PasswordField('Password', validators=[InputRequired(), Length(max=50)])
    confirm = PasswordField('Confirm Password',validators=[InputRequired()])
    accept_tos = BooleanField('I accept the User Agreement', validators=[InputRequired()])
    submit = SubmitField('Register')
