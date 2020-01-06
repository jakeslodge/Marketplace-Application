from flask import ( 
    Blueprint, flash, render_template, request, url_for, redirect
) 
from .models import User
from .forms import LoginForm, RegisterForm
from . import db
from flask_login import login_user, login_required,logout_user
#for password storage
from werkzeug.security import generate_password_hash,check_password_hash

#create a blueprint
bp = Blueprint('auth', __name__)

@bp.route('/login', methods = ['GET', 'POST'])
def login():
  form = LoginForm()
  error=None
  if(form.validate_on_submit()):
    user_name = form.username.data
    password = form.password.data
    u1 = User.query.filter_by(name=user_name).first()
    
        #if there is no user with that name
    if u1 is None:
      error='Incorrect user name'
    #check the password - notice password hash function
    elif not check_password_hash(u1.password_hash, password): # takes the hash and password
      error='Incorrect password'
    if error is None:
    #all good, set the login_user
      login_user(u1)
      return redirect(url_for('main.index'))
    else:
      print(error)
      flash(error)
    #it comes here when it is a get method
  return render_template('user_form.html', form=form, heading='Login')


@bp.route('/register', methods = ['GET', 'POST'])  
def register():  
    form = RegisterForm()
    if form.validate_on_submit():
      print('Register form submitted')
       
            #get username, password and email from the form
      uname =form.username.data
      pwd = form.password.data
      email=form.email.data
            # don't store the password - create password hash
      pwd_hash = generate_password_hash(pwd)
      #create a new user model object

      u1 = User.query.filter_by(name=uname).first()
      if u1 is None:
        new_user = User(name=uname, password_hash=pwd_hash, emailid=email)
        db.session.add(new_user)
        db.session.commit()
            #commit to the database and redirect to HTML page
      return redirect(url_for('auth.register'))
    
    
    return render_template('user_form.html', form=form, heading='Register')

@bp.route('/logout')
@login_required
def logout():
  logout_user()
  return 'You have been logged out'