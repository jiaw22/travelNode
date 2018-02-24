from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class PathForm(FlaskForm):
    location1 = StringField('Location 1', validators=[DataRequired()])
    location2 = StringField('Location 2', validators=[DataRequired()])
    location3 = StringField('Location 3', validators=[])
    location4 = StringField('Location 4', validators=[])
    location5 = StringField('Location 5', validators=[])
    currentTime = DateTimeField('Current Time', validators=[DataRequired()])
    active = RadioField('How active are you? (Less active-prefer uber, More active-walking)',
                        choices=[('1','Less Active'),('2','Moderately Active'),('3','Very Active')])
    haveVehicle = BooleanField('I have a personal vehicle.')
    submit = SubmitField('Submit field')

class SuggestionForm(FlaskForm):
    likedRoute = BooleanField('I did not like this route!')
    submit = SubmitField('Submit field')
