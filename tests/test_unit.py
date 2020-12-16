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
        self.assertIn(b"2000", response.data)

class TestReadCustomerHome(TestBase):
    def test_read_customer_home(self):
        response = self.client.get(
            url_for('customer_home'))
        self.assertIn(b"Rexx", response.data)
        self.assertIn(b"Barclays", response.data)
        self.assertIn(b"2000", response.data)

class TestAdd(TestBase):
    def test_add_account(self):
        response = self.client.post(
            url_for('addAccount'),
            data = dict(balance=2520, account="Natwest", customer="Renato", transaction_amount=2520),
            follow_redirects=True
        )
        self.assertIn(b'Natwest',response.data)
        self.assertIn(b'Renato',response.data)
        self.assertIn(b'2520',response.data)

class TestReadComplete(TestBase):
    def test_read_complete(self):
        response = self.client.post(
            url_for('complete', id=1, st_id=1),
            follow_redirects=True
        )
        self.assertIn(b"Barclays", response.data)
        self.assertIn(b"2000", response.data)
        self.assertIn(b"incomplete", response.data)

class TestReadIncomplete(TestBase):
    def test_read_incomplete(self):
        response = self.client.post(
            url_for('incomplete', id=1, st_id=1),
            follow_redirects=True
        )
        self.assertIn(b"Barclays", response.data)
        self.assertIn(b"2000", response.data)
        self.assertIn(b"complete", response.data)

class TestReadDeposit(TestBase):
    def test_deposit(self):
        response = self.client.post(
            url_for('deposit', account_id=1),
            data = dict(transaction="Got Credit",transaction_amount=100),
            follow_redirects=True
        )
        self.assertIn(b"100", response.data)

class TestReadWithdraw(TestBase):
    def test_withdraw(self):
        response = self.client.post(
            url_for('withdraw', account_id=1),
            data = dict(transaction="Buy tomatoes",transaction_amount=200),
            follow_redirects=True
        )
        self.assertIn(b"200", response.data)

class TestUpdate(TestBase):
    def test_update_account(self):
        response = self.client.post(
            url_for('update', id=1),
            data = dict(account="Wema", customer="Rexx"),
            follow_redirects=True
            )
        self.assertIn(b'Wema',response.data)
        self.assertIn(b'Rexx',response.data)



class TestStatements(TestBase):
    def test_statements(self):
        response = self.client.get(
            url_for('statements', id=1),
            )
        self.assertIn(b'Barclays',response.data)
        self.assertIn(b'Rexx',response.data)
        self.assertIn(b'2000',response.data)

class TestSortStatements(TestBase):
    def test_sort_statements(self):
        response = self.client.get(
            url_for('sortStatements', id=1),
            )
        self.assertIn(b'Barclays',response.data)
        self.assertIn(b'Rexx',response.data)
        self.assertIn(b'2000',response.data)

class TestSortStatementsDesc(TestBase):
    def test_sort_statements_desc(self):
        response = self.client.get(
            url_for('sortStatementsDesc', id=1),
            )
        self.assertIn(b'Barclays',response.data)
        self.assertIn(b'Rexx',response.data)
        self.assertIn(b'2000',response.data)

class TestSortStatementsAmount(TestBase):
    def test_sort_statements_amount(self):
        response = self.client.get(
            url_for('sortStatementsAmount', id=1),
            )
        self.assertIn(b'Barclays',response.data)
        self.assertIn(b'Rexx',response.data)
        self.assertIn(b'2000',response.data)

class TestSortStatementsAmountDesc(TestBase):
    def test_sort_statements_amount_desc(self):
        response = self.client.get(
            url_for('sortStatementsAmountDesc', id=1),
            )
        self.assertIn(b'Barclays',response.data)
        self.assertIn(b'Rexx',response.data)
        self.assertIn(b'2000',response.data)

class TestDeleteTransaction(TestBase):
    def test_delete_transaction(self):
        response = self.client.get(
            url_for('deleteTransaction', id=1, account_id=1),
            follow_redirects=True
            )
        self.assertNotIn(b'100',response.data)

class TestDelete(TestBase):
    def test_delete_account(self):
        response = self.client.get(
            url_for('delete', id=1),
            follow_redirects=True
            )
        self.assertNotIn(b'Barclays',response.data)
        self.assertNotIn(b'Rexx',response.data)
