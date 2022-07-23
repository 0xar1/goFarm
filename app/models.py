from app import db,login
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin,db.Model):
    uid = db.Column(db.Integer, primary_key=True)
    # username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(200))
    verified = db.Column(db.Boolean, default=False, nullable=False)
    full_name = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<User {}>'.format(self.email)
    def get_id(self):
           return (self.uid)

@login.user_loader
def load_user(uid):
    return User.query.get(int(uid))