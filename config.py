import os
from urllib.parse import quote
class Config(object):
     SECRET_KEY = os.environ.get('SECRET_KEY') or 'i123he98skdq'
     # MYSQL_USER = 'root'
     # MYSQL_PASSWORD = 'passwordroot691'
     # MYSQL_DB = 'app'
     # MYSQL_HOST = 'localhost'
     SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:%s@localhost/app' % quote('')
     SQLALCHEMY_TRACK_MODIFICATIONS = False