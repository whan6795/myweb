# encoding:utf-8
from exts import db
from datetime import datetime


class StoreUsers(db.Model):  # 商城用户
    __tablename__ = 'store_user'
    uid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(50), nullable=False)
    money = db.Column(db.String(50), nullable=False, default=0)


class Commodity(db.Model):  # 商品
    __tablename__ = 'commodity'
    uid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Integer, nullable=True)
    picture = db.Column(db.String(150), nullable=False)
    remain_num = db.Column(db.Integer, nullable=False)
    add_user_id = db.Column(db.Integer, nullable=False)
    detail = db.Column(db.Text)
