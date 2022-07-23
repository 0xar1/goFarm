from flask import Flask
from config import Config



app = Flask(__name__)
#importing the secret key file
app.config.from_object(Config)

#SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
db = SQLAlchemy(app)
migrate = Migrate(app,db)

#flask login
from flask_login import LoginManager
login = LoginManager(app)
login.login_view = 'auth.login'

#importing all routes,models and blueprints
from app import routes,models
from app.blueprints.auth import auth 
app.register_blueprint(auth)



# app.debug(True)   
