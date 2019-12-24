from flask_login import UserMixin
from .app import db 


class User(UserMixin , db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True,nullable=True )
    password = db.Column(db.String(100),nullable=False)
    name = db.Column(db.String(1000),nullable=False )
    role = db.Column(db.Integer,db.ForeignKey('role.id'),nullable=False)

class Role(UserMixin , db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_role = db.Column(db.String(20), unique=True, nullable=False)
