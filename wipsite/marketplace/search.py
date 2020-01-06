#function for getting search results and printing them
from flask import(Blueprint,flash,render_template,request,url_for,redirect)
from .models import Listing, User,Bid #import out classes
from . import db #import the database

bp = Blueprint('search',__name__,url_prefix='/search')

#have the route of the to generate the results
@bp.route('/<id>',methods=['GET','POST'])
def show(id):
    results = Listing.query.filter_by(genre=id).all() #take the Id of the genre given and show the results
    print(results)
    #send the results to rendered in results.html
    return render_template('results/show.html',results = results)

