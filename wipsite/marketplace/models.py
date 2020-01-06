from . import db
from datetime import datetime
from flask_login import UserMixin
from sqlalchemy.orm import relationship


class User(db.Model,UserMixin):
    __tablename__='users' #table naming
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100),index=True,unique=True,nullable=False)
    emailid = db.Column(db.String(100),index=True,nullable=False)
    password_hash = db.Column(db.String(255),nullable=False)

    #bids = db.relationship('Bid',backref='user')

    def __repr__(self):
        return "<Name: {}, ID: {}>".format(self.name, self.id)

class Listing(db.Model):
    __tablename__ = 'listings'
    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer) # added the owner id which will be logged in user id
    owner_name = db.Column(db.String) # owner name
    genre = db.Column(db.String)
    name = db.Column(db.String(80))
    description = db.Column(db.String(400))
    image = db.Column(db.String(400))
    price = db.Column(db.Integer)
    availability = db.Column(db.Boolean,default=True)
    #status = db.Column(db.String(15))
    # ... Create the Comments db.relationship
	# relation to call destination.comments and comment.destination
    # realtion to call listing.bids and bid.listing
    #create the reference to bid
    bids = db.relationship('Bid',backref='listing')

    def __repr__(self): #string print method
        return "<Name: {}>".format(self.name)

class Bid(db.Model):
    __tablename__ = 'bids'
    id = db.Column(db.Integer, primary_key=True)
    #add the foreign keys

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user_name = db.Column(db.String,db.ForeignKey('users.name'))

    user_email = db.Column(db.String)
    listing_id = db.Column(db.Integer, db.ForeignKey('listings.id'))
    bid_price = db.Column(db.Integer)
    create_at = db.Column(db.DateTime, default=datetime.now())

    #def __repr__(self): #use this when its called it returns the reference garbage
        #return"[{},{},{}]".format(self.user_id,self.bid_price,self.create_at)
    def returnInfo(self):
        bidinfo = []
        bidinfo.append(self.user_id)
        bidinfo.append(self.user_email)
        bidinfo.append(self.bid_price)
        bidinfo.append(self.create_at)

class Transaction(db.Model):
    __tablename__ = 'transactions'
    id = db.Column(db.Integer, primary_key = True)
    item_name = db.Column(db.String)
    seller_id = db.Column(db.Integer)
    seller_name = db.Column(db.String)
    buyer_id = db.Column(db.Integer)
    buyer_name = db.Column(db.String)
    sold_at = db.Column(db.DateTime, default=datetime.now())
    sold_for = db.Column(db.Integer) 