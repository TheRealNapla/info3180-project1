from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed

class PropertyForm(FlaskForm):
    title = StringField('Title', validators= [DataRequired()])
    desc = TextAreaField('Description', validators=[DataRequired()])
    bedsno = IntegerField('Number of Bedrooms', validators= [DataRequired()])
    bathsno = IntegerField('Number of Bathrooms', validators= [DataRequired()])
    price = StringField('Price', validators= [DataRequired()])
    propertytype = SelectField('Type of Property', choices=[
                         ('House', 'House'), ('Apartment', 'Apartment')], validators=[DataRequired()])
    location = StringField('Location', validators= [DataRequired()])
    pic = FileField('Photo', validators=[FileRequired(), FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Add Property')