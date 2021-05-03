# encoding:utf-8
from exts import db
from datetime import datetime


class Users(db.Model):
    __tablename__ = 'user'
    uid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(50), nullable=False)
    type = db.Column(db.Integer, nullable=False)

