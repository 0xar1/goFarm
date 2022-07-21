from flask import Flask
from config import Config



app = Flask(__name__)
#importing the secret key file
app.config.from_object(Config)


#importing the routes.py file
from app import routes

from app.blueprints.auth import auth 
app.register_blueprint(auth)

app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'passwordroot69'
app.config['MYSQL_DB'] = 'app'
app.config['MYSQL_HOST'] = 'localhost'

# app.debug(True)   
