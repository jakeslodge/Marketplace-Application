from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField,SubmitField,StringField, PasswordField,SelectField,IntegerField
from wtforms.validators import InputRequired, Length, Email, EqualTo

#form for adding a listing
class ListingForm(FlaskForm):
    name = StringField('Title',validators=[InputRequired()])

    #genre functionality
    genre = SelectField(u'Genre',choices=[ ('Action','Action'),('Kids','Kids'), ('Romance','Romance'),('Horror','Horror'),('Sci-Fi','Sci-Fi'),('Drama','Drama'),('Adventure','Adventure')])

    description = TextAreaField('Description',validators=[InputRequired()])
    image = StringField('Image URL',validators=[InputRequired()])
    price = IntegerField('Price',validators=[InputRequired()])
    submit = SubmitField("Create")

class BiddingForm(FlaskForm):
    ammount = IntegerField('Bid:',validators=[InputRequired()])
    submit = SubmitField("Place Bid")


class LoginForm(FlaskForm):
  username = StringField('User Name', validators=[InputRequired()])
  password = PasswordField('Password', validators=[InputRequired()])
  submit = SubmitField('Login')


class RegisterForm(FlaskForm):
  username = StringField('User Name', validators=[InputRequired()])
  email = StringField('Email ID', validators=[InputRequired(),Email() ])
  #password field
  password = PasswordField('Password', validators=[InputRequired()])
  #validator to check if the user entry is equal to password
  confirm = PasswordField('Confirm Password', 
          validators=[EqualTo('password', message='Re-enter same as Password')])
  submit = SubmitField('Register')

class TransactionForm(FlaskForm):
  soldTo = SelectField('Sold To:')
  soldPrice = IntegerField('Sold For:',validators=[InputRequired()])
  submit = SubmitField('Sell')
  