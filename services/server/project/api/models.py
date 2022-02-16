import datetime

from flask import current_app
#from flask_login import LoginManager, UserMixin
from sqlalchemy.sql import func

from project import db

class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(256))

    def __init__(self, password, email):
        self.email = email
        self.password = password

    def to_json(self):
        return {
            'id': self.id,
            'email': self.email,
            'password': self.password
        }
