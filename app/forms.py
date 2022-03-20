from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import *
from flask_wtf.file import *

class Create(FlaskForm):

    title = StringField('Title', [InputRequired()])
    beds = IntegerField('Bedrooms', [InputRequired(), NumberRange(0)])
    baths = IntegerField('Bathrooms', [InputRequired(), NumberRange(0)])
    location = StringField('Location', [InputRequired()])
    price = DecimalField('Price',[InputRequired()],places=2,rounding=2)
    type = SelectField('Type',[InputRequired()],choices=[('House','House'), ('Apartment','Apartment')])
    description = TextAreaField('Description',[DataRequired(), Length(max=255)])
    pic = FileField('image', [DataRequired(), FileAllowed(['jpg', 'jpeg', 'png'], 'Images Only!')])