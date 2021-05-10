from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class GoogleSearchForm(FlaskForm):
    period = StringField('Period',
                           validators=[DataRequired()])
    keyword = StringField('Keyword',
                        validators=[DataRequired()])
    submit = SubmitField('Search')
