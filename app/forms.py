from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed

class PropertyForm(FlaskForm):
    title = StringField('Title', validators= [DataRequired()])
    bedsno = StringField('Number of Bedrooms', validators= [DataRequired()])
    bathsno = StringField('Number of Bathrooms', validators= [DataRequired()])
    location = StringField('Location', validators= [DataRequired()])
    price = StringField('Price', validators= [DataRequired()])
    propertytype = SelectField('Type of Property', choices=[
                         ('House', 'House'), ('Apartment', 'Apartment')], validators=[DataRequired()])
    desc = TextAreaField('Description', validators=[DataRequired()])
    pic = FileField('Photo', validators=[FileRequired(), FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Add Property')