#this function handles the routing and what information to pass to the manage page
#function for getting search results and printing them
from flask import(Blueprint,flash,render_template,request,url_for,redirect)
from .models import Listing, User,Bid,Transaction #import out classes
from . import db #import the database
from flask_login import current_user, login_required #use the users current id
from .forms import TransactionForm

bp = Blueprint('manage',__name__,url_prefix='/manage')

#sort the routing method
@bp.route('/')
@login_required
def showManage():
    print(str(current_user.id))
    print(type(current_user.id))
    usersItemsOnSale = Listing.query.filter_by(owner_id=current_user.id).all()
    print(type(usersItemsOnSale))
    return render_template('manage/show2.html', itemsOnSale=usersItemsOnSale)

@bp.route('/<id>',methods=['GET','POST'])
@login_required
def manageItem(id):
    listingBeingManaged = Listing.query.filter_by(id=id).first()
    form = TransactionForm()
    form.soldTo.choices = [(g.user_name,g.user_name) for g in listingBeingManaged.bids]

    #check if the form is valid
    if form.validate_on_submit():

        #lets find the id of the other guys name
        buyer = User.query.filter_by(name=form.soldTo.data).first()
        buyerID = buyer.id
        listing = Listing.query.filter_by(id=id).first()
        listing.availability=False
        transaction = Transaction(item_name=listing.name,seller_id=current_user.id,seller_name=current_user.name,buyer_id=buyerID,buyer_name=form.soldTo.data,sold_for=form.soldPrice.data)
        db.session.add(transaction)
        db.session.commit()
        #return redirect(url_for('view.index'))
        #return render_template('index.html')
        return redirect(url_for('main.index')) 

    return render_template('manage/editsale.html',form=form,listingOnSale=listingBeingManaged)
