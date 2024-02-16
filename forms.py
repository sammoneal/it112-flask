from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FloatField, SelectField, DecimalField
from wtforms.validators import InputRequired, DataRequired, NumberRange


class RecipeAdd(FlaskForm):
    name = StringField("Name", validators=[InputRequired()])
    author = StringField("Author")
    description = TextAreaField("Description")
    ingredients = TextAreaField("Ingredients", validators=[InputRequired()])
    instructions = TextAreaField("Instructions", validators=[InputRequired()])
    rating = FloatField("Rating")
    category_id = SelectField("Category", coerce=int, validators=[InputRequired()])


#RECIPE EDIT FORM
class RecipeEdit(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    ingredients = TextAreaField('Ingredients', validators=[DataRequired()])
    instructions = TextAreaField('Instructions', validators=[DataRequired()])
    category_id = SelectField('Category', coerce=int, validators=[DataRequired()])
    rating = DecimalField('Rating', validators=[NumberRange(min=0, max=5)])
