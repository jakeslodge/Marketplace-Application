from flask import(Blueprint,flash,render_template,request,url_for,redirect)
from .models import Listing, User,Bid #import out classes
from .forms import ListingForm, BiddingForm #import the listing form
from . import db #import the database
from flask_login import current_user, login_required


#ceate a blueprint
bp = Blueprint('listings',__name__,url_prefix='/listings')

#create a page that will show information of that listing
@bp.route('/<id>',methods=['GET','POST'])
@login_required
def show(id):
    #temporal_id = str(id)
    listing = Listing.query.filter_by(id=id).first()
    USERID = current_user.id
    print(listing)
    if listing == None:
        print("give 404")
        return render_template('listings/404.html')
    cform = ListingForm()
    bform = BiddingForm()
    if bform.validate_on_submit():
        #if the form sent update the link
        print("a bid has been placed on:"+str(id)+" by "+str(current_user.id)+" for: "+str(bform.ammount))
        newbid = Bid(user_id=current_user.id,user_name=current_user.name,user_email=current_user.emailid,listing_id=int(id),bid_price=bform.ammount.data)
        db.session.add(newbid)
        db.session.commit()
        return redirect(request.url)#redirect to the self page once a bid is submitted
        #add function to test if user.id == to listing.owner.id, cannot bid

    return render_template('listings/show2.html',listing = listing, form=cform,BidForm=bform,USERID=USERID)

@bp.route('/create',methods=['GET','POST'])
@login_required
def create():
    form = ListingForm()
    if form.validate_on_submit():
        #if the form validates
        #take the info from the form and add it to the db
        listing = Listing(owner_id=current_user.id,owner_name=current_user.name,genre=form.genre.data,name=form.name.data,description=form.description.data,image=form.image.data,price=form.price.data)
        # add the object to the database
        db.session.add(listing)
        #commit the change
        db.session.commit()
        print('You add a new listing!')
        return redirect(url_for('listings.create'))
    return render_template('listings/create.html',form=form)