from flask import Blueprint,render_template
from flask import request
from flask import session
from flask_login import login_required
from . import db #import the database
from .models import Listing, User,Bid #import out classes


#create a blueprint
mybp = Blueprint('main',__name__)

#register the route with the blue print
@mybp.route('/')
@login_required
def index():
    dvdlistings = Listing.query.all()
    dvdlistings = Listing.query.order_by(Listing.id.desc()).all() # get the most recent 3
    return render_template('index.html',listings = dvdlistings)