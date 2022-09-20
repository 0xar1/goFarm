from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField,DateTimeField, SubmitField, validators,ValidationError
from wtforms_sqlalchemy.fields import QuerySelectField
from wtforms.fields import DateTimeLocalField
from wtforms.validators import Email, InputRequired, Length, EqualTo
from .models import Crops
from datetime import datetime

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    password = PasswordField('Password', validators=[InputRequired(),  Length(min=6,max=50)])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegisterForm(FlaskForm):   
    fullname = StringField('Username',validators=[InputRequired(), Length(max=50)]) 
    email = StringField('Email', validators=[InputRequired(), Email(message='Invalid email'), Length(min=6,max=50)])
    password = PasswordField('Password', validators=[InputRequired(), Length(max=50)])
    confirm = PasswordField('Confirm Password',validators=[InputRequired()])
    accept_tos = BooleanField('I accept the User Agreement', validators=[InputRequired()])
    submit = SubmitField('Register')

def cropname_choice():
    return Crops.query.distinct('name')

class SellForm(FlaskForm):
    cropname = QuerySelectField(query_factory=cropname_choice, allow_blank=False,get_label = 'name')
    variety = StringField('Variety',validators=[InputRequired(), Length(max=50)])
    amount = StringField('Amount',validators=[InputRequired(), Length(max=50)])
    minprice = StringField('Minimum Price',validators=[InputRequired(), Length(max=50)])
    datetime = DateTimeLocalField('Date (DD-MM-YYYY)', format='%Y-%m-%dT%H:%M')
    submit = SubmitField('Submit')
    # def validate_date(self,date):
    #     if f
