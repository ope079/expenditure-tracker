import unittest
from flask import url_for
from flask_testing import TestCase

from application import app, db
from application.models import Accounts, Transaction

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///test.db",
                SECRET_KEY='TEST_SECRET_KEY',
                DEBUG=True
                )
        return app

    def setUp(self):
        db.create_all()
        test_account = Accounts(account_name="Barclays",cust_name="Rexx", balance=2000 )
        test_transaction = Transaction(transaction="Buy grapes", transaction_amount="20", accounts=test_account )
        db.session.add(test_account)
        db.session.add(test_transaction)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestViews(TestBase):

    def test_home_get(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)

    def test_add_account_get(self):
        response = self.client.get(url_for('addAccount'))
        self.assertEqual(response.status_code,200)

    def test_customer_home_get(self):
        response = self.client.get(url_for('customer_home'))
        self.assertEqual(response.status_code, 200)
       
    def test_complete_get(self):
        response = self.client.get(url_for('complete', id=1, st_id=1), follow_redirects=True)
        self.assertEqual(response.status_code,200)
    
    def test_incomplete_get(self):
        response = self.client.get(url_for('incomplete', id=1, st_id=1), follow_redirects=True)
        self.assertEqual(response.status_code,200)

    def test_update_account_information_get(self):
        response = self.client.get(url_for('update', id=1), follow_redirects=True)
        self.assertEqual(response.status_code,200)
    
    def test_deposit_get(self):
        response = self.client.get(url_for('deposit', account_id=1), follow_redirects=True)
        self.assertEqual(response.status_code,200)
    
    def test_withdraw_get(self):
        response = self.client.get(url_for('withdraw', account_id=1), follow_redirects=True)
        self.assertEqual(response.status_code,200)

    def test_deletetransaction_get(self):
        response = self.client.get(url_for('deleteTransaction', id=1, account_id=1), follow_redirects=True)
        self.assertEqual(response.status_code,200)
    
    def test_delete_get(self):
        response = self.client.get(url_for('delete', id=1), follow_redirects=True)
        self.assertEqual(response.status_code,200)

    def test_statements_get(self):
        response = self.client.get(url_for('statements', id=1))
        self.assertEqual(response.status_code, 200)

    def test_sortStatements_get(self):
        response = self.client.get(url_for('sortStatements', id=1))
        self.assertEqual(response.status_code, 200)

    def test_sortStatementsDes_get(self):
        response = self.client.get(url_for('sortStatementsDesc', id=1))
        self.assertEqual(response.status_code, 200)

    def test_sortStatementsAmount_get(self):
        response = self.client.get(url_for('sortStatementsAmount', id=1))
        self.assertEqual(response.status_code, 200)

    def test_sortSatementsAmountDesc_get(self):
        response = self.client.get(url_for('sortStatementsAmountDesc', id=1))
        self.assertEqual(response.status_code, 200)
 
class TestRead(TestBase):
    def test_read_accounts(self):
        response = self.client.get(
            url_for('home'))
        self.assertIn(b"Barclays", response.data)
        self.assertIn(b"000", response.data)
 
class TestAdd(TestBase):
    def test_add_account(self):
        response = self.client.post(
            url_for('addAccount'),
            data = dict(balance=2520, account="Natwest", customer="Renato" ),
            follow_redirects=True
        )
        self.assertIn(b'Natwest',response.data)
        self.assertIn(b'Renato',response.data)
        self.assertIn(b'2520',response.data)

class TestUpdate(TestBase):
    def test_update_account(self):
        response = self.client.post(
            url_for('update', id=1),
            data = dict(account="Wema", customer="Rexx"),
            follow_redirects=True
            )
        self.assertIn(b'Wema',response.data)
        self.assertIn(b'Rexx',response.data)

class TestDelete(TestBase):
    def test_delete_account(self):
        response = self.client.get(
            url_for('delete', id=1),
            follow_redirects=True
            )
        self.assertNotIn(b'Barclays',response.data)
        self.assertNotIn(b'Rexx',response.data)
        self.assertNotIn(b'2000',response.data)
