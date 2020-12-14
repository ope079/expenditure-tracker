from flask_wtf import FlaskForm
from wtforms import StringField, DateField, IntegerField, DecimalField, SelectField, SubmitField
from wtforms.validators import DataRequired, InputRequired

class HomeForm(FlaskForm):
    account = StringField('Enter Account Name', validators=[DataRequired()])
    customer = StringField('Enter your preferred Name', validators=[DataRequired()])
    balance = IntegerField('Enter Initial Balance', validators=[DataRequired()])
    submit = SubmitField('Add the Account')

class TransactionForm(FlaskForm):
    transaction = StringField('Enter the transaction here' , validators=[DataRequired()])
    transaction_amount = IntegerField('Enter the transaction Amount', validators=[DataRequired()])
    submit = SubmitField('Add the Transaction')