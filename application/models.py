from application import db
from datetime import datetime



class Accounts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    balance = db.Column(db.Integer)
    account_name = db.Column(db.String(30), nullable=False)
    cust_name = db.Column(db.String(30), nullable=False)
    transactions = db.relationship('Transaction', backref='accounts' , lazy='dynamic')


class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    transaction = db.Column(db.String(50), nullable=False)
    transaction_amount = db.Column(db.Integer)
    transaction_completed = db.Column(db.Boolean, nullable=False, default=False)
    transaction_date= db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    accounts_id = db.Column(db.Integer, db.ForeignKey('accounts.id'), nullable=False)