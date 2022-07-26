from . import db,login
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
    sellerId = db.relationship('Auction', backref='user')

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

class Crops(db.Model):
    name = db.Column(db.String(50))
    cropId = db.Column(db.Integer, primary_key = True)
    variety = db.Column(db.String(50))
    # def __repr__(self):
        # return self.name

class Auction(db.Model):
    aid = db.Column(db.Integer, primary_key = True)
    sellerName = db.Column(db.String(50))
    cropName = db.Column(db.String(50))
    sellerId = db.Column(db.Integer, db.ForeignKey('user.uid'))
    cropId = db.Column(db.Integer,db.ForeignKey('crops.cropId'))
    variety = db.Column(db.String(50))
    minPrice = db.Column(db.Integer)
    datetime = db.Column(db.DateTime, index=True, nullable = False)
    currentBid = db.Column(db.Integer,default = 0)

    def __repr__(self):
        return self.datetime

class CurrentAuction(db.Model):
    aid = db.Column(db.Integer, primary_key = True)
    sellerName = db.Column(db.String(50))
    cropName = db.Column(db.String(50))
    sellerId = db.Column(db.Integer, db.ForeignKey('user.uid'))
    cropId = db.Column(db.Integer,db.ForeignKey('crops.cropId'))
    variety = db.Column(db.String(50))
    minPrice = db.Column(db.Integer)
    datetime = db.Column(db.DateTime, index=True, nullable = False)
    currentBid = db.Column(db.Integer,default = 0)
    
class tempTable(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    aid = db.Column(db.Integer)
    userBid = db.Column(db.Integer,default = 0)
    buyerid = db.Column(db.Integer)
    buyerName = db.Column(db.String(50))

class Ledger(db.Model):
    aid = db.Column(db.Integer, primary_key = True)
    sellerId = db.Column(db.Integer)
    buyerId = db.Column(db.Integer)
    price = db.Column(db.Integer)
    datetime = db.Column(db.DateTime, index=True, nullable = False)


