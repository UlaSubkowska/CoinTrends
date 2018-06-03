from flask_wtf import FlaskForm
from wtforms import BooleanField, SubmitField, DateField
from wtforms.validators import DataRequired

class GetDate(FlaskForm):
    start_date = DateField('Start date', validators=[DataRequired()])
    end_date = DateField('End date', validators=[DataRequired()])
    trends=BooleanField('Display trends', default=False)
    submit = SubmitField('Display')