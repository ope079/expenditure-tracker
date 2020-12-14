from application import app, db
from application.models import Accounts, Transaction
from application.forms import HomeForm, TransactionForm
from flask import render_template, request, redirect, url_for
 

@app.route('/')
@app.route('/home')
def home():
    all_accounts = Accounts.query.all()
    account_string = ""
    return render_template("index.html", title="Home", all_accounts=all_accounts)

@app.route('/add_account', methods=['GET','POST'])   
def addAccount():
    form = HomeForm()
    if request.method == "POST":
        if form.validate_on_submit():
            new_account = Accounts(account_name=form.account.data,cust_name=form.customer.data, balance=form.balance.data)
            new_transaction = Transaction(transaction="Initial Balance", transaction_amount=form.balance.data, accounts=new_account)
            db.session.add(new_account)
            db.session.add(new_transaction)
            db.session.commit()
            return redirect(url_for("customer_home"))
    return render_template("add_account.html", title="Add a new Account", form=form)

@app.route('/customer_home')
def customer_home():
    all_accounts = Accounts.query.all()
    account_string = ""
    return render_template("customer_home.html", title="CustomerHome", all_accounts=all_accounts)

@app.route('/complete/<int:id>/<int:st_id>', methods=['GET','POST'])
def complete(id, st_id):
    account = Accounts.query.filter_by(id=id).first()
    transaction = account.transactions.filter_by(id=st_id).first()
    transaction.transaction_completed = True
    db.session.commit()
    return redirect(url_for("statements", id=id, st_id=st_id))

@app.route('/incomplete/<int:id>/<int:st_id>', methods=['GET','POST'])
def incomplete(id, st_id):
    account = Accounts.query.filter_by(id=id).first()
    transaction = account.transactions.filter_by(id=st_id).first()
    transaction.transaction_completed = False
    db.session.commit()
    return redirect(url_for("statements", id=id, st_id=st_id))


@app.route('/add_payee_information/<int:id>', methods=['GET','POST'])   
def add(id):
    account = Accounts.query.filter_by(id=id).first()
    form = TransactionForm()
    if request.method == "POST":
        if form.validate_on_submit():
            new_transaction = Transaction(transaction=form.transaction.data,transaction_amount=form.transaction_amount.data, accounts=account)
            db.session.add(new_transaction)
            db.session.commit()
            return redirect(url_for("home"))
    return render_template("add_payee_information.html", title="Add a transaction", form=form)

@app.route('/update_payee_information/<int:id>',  methods=['GET','POST'])
def update(id):
    form = TransactionForm()
    transaction = Transaction.query.filter_by(id=id).first()
    if request.method =="POST":
        transaction.transaction = form.transaction.data
        transaction.amount = form.transaction_amount.data
        db.session.commit()
        return redirect(url_for("customer_home"))
    return render_template("update_payee_information.html", form=form, title="Update Transaction", transaction=transaction)

@app.route('/deposit/<int:account_id>',  methods=['GET','POST'])
def deposit(account_id):
    form = TransactionForm()
    account = Accounts.query.filter_by(id=account_id).first()
    
    if request.method =="POST":
        if form.validate_on_submit():
            deposit =  Transaction(transaction="Deposit : "+form.transaction.data,transaction_amount=form.transaction_amount.data, accounts=account)
            db.session.add(deposit)
            account.balance = account.balance + form.transaction_amount.data
            db.session.commit()
            return redirect(url_for("customer_home"))
    return render_template("deposit.html", form=form, title="Add Deposit" , account=account)

@app.route('/withdraw/<int:account_id>',  methods=['GET','POST'])
def withdraw(account_id):
    form = TransactionForm()
    account = Accounts.query.filter_by(id=account_id).first()
    
    if request.method =="POST":
        if form.validate_on_submit():
            deposit =  Transaction(transaction="Withdrawal : "+form.transaction.data,transaction_amount=form.transaction_amount.data, accounts=account)
            db.session.add(deposit)
            account.balance = account.balance - form.transaction_amount.data
            db.session.commit()
            return redirect(url_for("customer_home"))
    return render_template("withdraw.html", form=form, title="Add Withdrawal" , account=account)

@app.route('/delete/<int:id>')
def delete(id):
    transaction = Transaction.query.filter_by(id=id).first()
    db.session.delete(transaction)
    db.session.commit()
    return redirect(url_for("home"))

@app.route('/statements/<int:id>', methods=['GET'])
def statements(id):
    account = Accounts.query.filter_by(id=id).first()
    statements = account.transactions.all()
    return render_template("statements.html", title="Statements", statements=statements, account=account)


