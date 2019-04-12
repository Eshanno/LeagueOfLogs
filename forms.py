from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField ,FileField
from wtforms.validators import DataRequired

class searchBarForm(FlaskForm):
    search = StringField("<h1>Search By Summoner Name<h1>", validators=[DataRequired()])
    submit = SubmitField('Submit')
