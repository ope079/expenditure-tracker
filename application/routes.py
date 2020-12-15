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


@app.route('/update_account_information/<int:id>',  methods=['GET','POST'])
def update(id):
    form = HomeForm()
    account = Accounts.query.filter_by(id=id).first()
    if request.method =="POST":
        account.account_name = form.account.data
        account.cust_name = form.customer.data
        db.session.commit()
        return redirect(url_for("customer_home"))
    return render_template("update_account_information.html", form=form, title="Update Account Information", account=account)

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


@app.route('/deleteTransaction/<int:id>/<int:account_id>')
def deleteTransaction(id, account_id):
    transaction = Transaction.query.filter_by(id=id).first()
    account = Accounts.query.filter_by(id=account_id).first()
    if transaction.transaction.startswith('Deposit'):
        account.balance = account.balance - transaction.transaction_amount
    elif transaction.transaction.startswith('Withdrawal'):
        account.balance = account.balance + transaction.transaction_amount
    db.session.delete(transaction)
    db.session.commit()
    return redirect(url_for("statements", id=account.id))

@app.route('/delete/<int:id>')
def delete(id):
    account = Accounts.query.filter_by(id=id).first()
    db.session.delete(account)
    db.session.commit()
    return redirect(url_for("customer_home"))

@app.route('/statements/<int:id>', methods=['GET'])
def statements(id):
    account = Accounts.query.filter_by(id=id).first()
    statements = account.transactions.all()
    return render_template("statements.html", title="Statements", statements=statements, account=account)

@app.route('/sortStatements/<int:id>', methods=['GET'])
def sortStatements(id):
    account = Accounts.query.filter_by(id=id).first()
    statements = account.transactions.order_by(Transaction.transaction_date).all()
    return render_template("statements.html", id=id, title="Statements", statements=statements, account=account)

@app.route('/sortStatementsDes/<int:id>', methods=['GET'])
def sortStatementsDesc(id):
    account = Accounts.query.filter_by(id=id).first()
    statements = account.transactions.order_by(Transaction.transaction_date.desc()).all()
    return render_template("statements.html", id=id, title="Statements", statements=statements, account=account)

@app.route('/sortStatementsAmount/<int:id>', methods=['GET'])
def sortStatementsAmount(id):
    account = Accounts.query.filter_by(id=id).first()
    statements = account.transactions.order_by(Transaction.transaction_amount).all()
    return render_template("statements.html", id=id, title="Statements", statements=statements, account=account)

@app.route('/sortStatementsAmountDesc/<int:id>', methods=['GET'])
def sortStatementsAmountDesc(id):
    account = Accounts.query.filter_by(id=id).first()
    statements = account.transactions.order_by(Transaction.transaction_amount.desc()).all()
    return render_template("statements.html", id=id, title="Statements", statements=statements, account=account)
