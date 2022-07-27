import os
from urllib.parse import quote
class Config(object):
     SECRET_KEY = os.environ.get('SECRET_KEY') or 'i123he98skdq'
     UPLOAD_FOLDER = 'static/uploads/'
     # MYSQL_USER = 'root'
     # MYSQL_PASSWORD = 'passwordroot691'
     # MYSQL_DB = 'app'
     # MYSQL_HOST = 'localhost'
     SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:%s@localhost/app' % quote('')
     SQLALCHEMY_TRACK_MODIFICATIONS = False
     MAIL_SERVER = 'smtp.gmail.com'
     MAIL_PORT = 465
     MAIL_USE_SSL = True
     MAIL_USERNAME = "floppafr@gmail.com"
     MAIL_PASSWORD = '%s'  % quote('Floppafr@2022')