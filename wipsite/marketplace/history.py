#this function handles the routing and what information to pass to the manage page
#function for getting search results and printing them
from flask import(Blueprint,flash,render_template,request,url_for,redirect)
from .models import Listing, User,Bid,Transaction #import out classes
from . import db #import the database
from flask_login import current_user,login_required #use the users current id
from .forms import TransactionForm

bp = Blueprint('history',__name__,url_prefix='/history')

#sort the routing method
@bp.route('/')
@login_required
def showHistory():
    print("history page")
    userSoldItems = Transaction.query.filter_by(seller_id=current_user.id).all()
    userBoughtItems = Transaction.query.filter_by(buyer_id=current_user.id).all()
    return render_template('history/show.html',sold=userSoldItems,bought=userBoughtItems)