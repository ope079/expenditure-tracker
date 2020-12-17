import unittest
import time
from flask import url_for
from urllib.request import urlopen

from os import getenv
from flask_testing import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from application import app, db
from application.models import Accounts, Transaction




class TestBase(LiveServerTestCase):

    def create_app(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = str(getenv('DATABASE_URI'))
        app.config['SECRET_KEY'] = getenv('SECRET_KEY')
        return app

    def setUp(self):
        print("--------------------------NEXT-TEST----------------------------------------------")
        #chrome_options = Options()
        #chrome_options.binary_location = "/usr/bin/chromium-browser"
        #chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(
            #executable_path="/home/o_orekoya/chromedriver", chrome_options=chrome_options
            )
        self.driver.get("http://localhost:5000")
        
        db.session.commit()
        db.drop_all()
        db.create_all()
        
        test_account = Accounts(account_name="Barclays",cust_name="Rexx", balance=2000 )
        test_transaction = Transaction(transaction="Buy grapes", transaction_amount="20", accounts=test_account )
        
        db.session.add(test_account)
        db.session.add(test_transaction)
        db.session.commit()
        

    def tearDown(self):


        self.driver.quit()
        print("--------------------------END-OF-TEST----------------------------------------------\n\n\n-------------------------UNIT-AND-SELENIUM-TESTS----------------------------------------------")

    def test_server_is_up_and_running(self):
        response = urlopen("http://localhost:5000")
        self.assertEqual(response.code, 200)

class TestAccountCreation(TestBase):

    def test_account_creation(self):
        """
        Test that a user can create an account
        """

        # Navigate to Add Account Page
        self.driver.find_element_by_xpath("/html/body/a[2]").click()
        time.sleep(1)

        # Input account information into form field
        self.driver.find_element_by_xpath('//*[@id="account"]').send_keys("Wema")
        self.driver.find_element_by_xpath('//*[@id="customer"]').send_keys("Rennie")
        self.driver.find_element_by_xpath('//*[@id="balance"]').send_keys("2500")
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        time.sleep(1)

        # Assert that browser redirects to customer home page
        assert url_for('customer_home') in self.driver.current_url
        new_account = Accounts.query.filter_by(id=2).first()
        assert new_account.account_name == "Wema"
        assert new_account.cust_name == "Rennie"

class TestUpdateAccount(TestBase):

    def test_update_account(self):
        """
        Test that a user can update an account
        """

        # Navigate to Update Account Page
        self.driver.find_element_by_xpath("/html/body/a[3]").click()
        self.driver.find_element_by_xpath("/html/body/a[4]").click()
        time.sleep(1)

        # Input account information into form field
        self.driver.find_element_by_xpath('//*[@id="account"]').send_keys("Natwest")
        self.driver.find_element_by_xpath('//*[@id="customer"]').send_keys("Rexxie")
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        time.sleep(1)

        # Assert that browser redirects to customer home page
        assert url_for('customer_home') in self.driver.current_url
        new_account = Accounts.query.filter_by(id=1).first()
        assert new_account.account_name == "Natwest"
        assert new_account.cust_name == "Rexxie"


class TestDeposit(TestBase):

    def test_deposit(self):
        """
        Test that a user can deposit in an account
        """

        # Navigate to Update deposit Page
        self.driver.find_element_by_xpath("/html/body/a[3]").click()
        self.driver.find_element_by_xpath("/html/body/form[2]/input").click()
        time.sleep(1)

        # Input account information into form field
        self.driver.find_element_by_xpath('//*[@id="transaction"]').send_keys("Sold apples")
        self.driver.find_element_by_xpath('//*[@id="transaction_amount"]').send_keys("20")
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        time.sleep(1)

        # Assert that browser redirects to customer home page
        assert url_for('customer_home') in self.driver.current_url
        new_account = Accounts.query.filter_by(id=1).first()
        assert new_account.balance == 2020

class TestWithdraw(TestBase):

    def test_withdraw(self):
        """
        Test that a user can withdraw from an account
        """

        # Navigate to Update withdraw Page
        self.driver.find_element_by_xpath("/html/body/a[3]").click()
        self.driver.find_element_by_xpath("/html/body/form[1]/input").click()
        time.sleep(1)

        # Input account information into form field
        self.driver.find_element_by_xpath('//*[@id="transaction"]').send_keys("Buy apples")
        self.driver.find_element_by_xpath('//*[@id="transaction_amount"]').send_keys("20")
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        time.sleep(1)

        # Assert that browser redirects to customer home page
        assert url_for('customer_home') in self.driver.current_url
        new_account = Accounts.query.filter_by(id=1).first()
        assert new_account.balance == 1980

class TestDeleteAccount(TestBase):

    def test_delete_account(self):
        """
        Test that a user can delete an account
        """

        # Navigate to Update Delete Page
        self.driver.find_element_by_xpath("/html/body/a[3]").click()
        self.driver.find_element_by_xpath("/html/body/form[3]/input").click()
        time.sleep(1)


        # Assert that browser redirects to customer home page
        assert url_for('customer_home') in self.driver.current_url

class TestDeleteTransaction(TestBase):

    def test_delete_transaction(self):
        """
        Test that a user can delete a transaction
        """

        # Navigate to Update Delete Page
        self.driver.find_element_by_xpath("/html/body/a[3]").click()
        self.driver.find_element_by_xpath("/html/body/a[3]").click()
        self.driver.find_element_by_xpath("/html/body/form[2]/input").click()
        time.sleep(1)


        # Assert that browser redirects to statements page
        assert url_for('statements', id=1) in self.driver.current_url    

class TestViewStatement(TestBase):

    def test_view_statement(self):
        """
        Test that a user can view statements
        """

        # Navigate to Update Delete Page
        self.driver.find_element_by_xpath("/html/body/a[3]").click()
        self.driver.find_element_by_xpath("/html/body/a[3]").click()
        time.sleep(1)


        # Assert that browser redirects to statements page
        assert url_for('statements', id=1) in self.driver.current_url

class TestComplete(TestBase):

    def test_complete(self):
        """
        Test that a user can mark a transaction complete
        """

        # Navigate to Update Delete Page
        self.driver.find_element_by_xpath("/html/body/a[3]").click()
        self.driver.find_element_by_xpath("/html/body/a[3]").click()
        self.driver.find_element_by_xpath("/html/body/form[1]/input").click()
        time.sleep(1)


        # Assert that browser redirects to statements page
        assert url_for('statements', id=1, st_id=1) in self.driver.current_url      
        transaction = Accounts.query.filter_by(id=1).first().transactions.filter_by(id=1).first()
        assert transaction.transaction_completed == True

class TestIncomplete(TestBase):

    def test_incomplete(self):
        """
        Test that a user can mark a transaction incomplete
        """

        # Navigate to Update Delete Page
        self.driver.find_element_by_xpath("/html/body/a[3]").click()
        self.driver.find_element_by_xpath("/html/body/a[3]").click()
        self.driver.find_element_by_xpath("/html/body/form[1]/input").click()
        self.driver.find_element_by_xpath("/html/body/form[1]/input").click()
        time.sleep(1)


        # Assert that browser redirects to statements page
        assert url_for('statements', id=1, st_id=1) in self.driver.current_url      
        transaction = Accounts.query.filter_by(id=1).first().transactions.filter_by(id=1).first()
        assert transaction.transaction_completed == False

if __name__ == '__main__':
    unittest.main(port=5000)