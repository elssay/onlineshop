from app import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), unique = True)
    name = db.Column(db.String(128))


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))
    price = db.Column(db.Integer)
    img_url = db.Column(db.String(128))
    created = db.Column(db.DateTime, default=datetime.now)