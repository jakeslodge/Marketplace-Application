from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
import os

from flask_login import LoginManager

db=SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.secret_key='hello'
    app.debug = True

    @app.errorhandler(404) 
    def not_found(e): 
        return render_template("404.html")

    @app.errorhandler(500)
    def internalError(e):
        return render_template("500.html")

    #database
    app.config['SQLALCHEMY_DATABASE_URI']=os.environ['DATABASE_URL']
    #initalize the app with flask
    db.init_app(app)

    bootstrap = Bootstrap(app)

    #add loging manager
    login_manager = LoginManager()

    #set the name of the loging fucntion the lets users log in
    login_manager.login_view='auth.login'
    login_manager.init_app(app)

    #create a user loader function takes userid and returns User
    from .models import User  # importing here to avoid circular references
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))


    from . import search #add the search functions
    app.register_blueprint(search.bp)

    from . import auth
    app.register_blueprint(auth.bp)

    from .views import mybp #import it so we can route
    app.register_blueprint(mybp)

    from . import listings
    app.register_blueprint(listings.bp)

    from . import manage
    app.register_blueprint(manage.bp)

    from . import history
    app.register_blueprint(history.bp)
    
    return app