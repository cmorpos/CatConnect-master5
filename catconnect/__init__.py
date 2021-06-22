from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cat.db'
app.config['SECRET_KEY'] = 'ce2d1a413c1a28102085afeb'
db = SQLAlchemy(app)

from catconnect import routes