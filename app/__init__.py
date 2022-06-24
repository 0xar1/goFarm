from flask import Flask
from requests import session
from config import Config



app = Flask(__name__)
#importing the secret key file
app.config.from_object(Config)

#importing the routes.py file
from app import routes

# app.debug(True)   
