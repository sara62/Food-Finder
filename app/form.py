from app import app
from wtforms import Form, StringField, BooleanField

class SearchForm(Form):
    search      = StringField('Search')
    location    = StringField('Location')
    haveCar     = BooleanField('haveCar')
