from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv

app = Flask(__name__)

db = SQLAlchemy(app)

app.config['SECRET_KEY'] = getenv("SECRET_KEY")

app.config['SQLALCHEMY_DATABASE_URI'] = getenv("DATABASE_URI")



from application import routes