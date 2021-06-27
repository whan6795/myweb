# encoding:utf-8
from exts import db
from datetime import datetime


class StoreUsers(db.Model):  # 商城用户
    __tablename__ = 'store_user'
    uid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(50), nullable=False)
    login_num = db.Column(db.Integer, default=0)
    last_login_time = db.Column(db.DateTime)
    login_time = db.Column(db.DateTime)


class Commodity(db.Model):  # 商品
    __tablename__ = 'commodity'
    uid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    picture = db.Column(db.LargeBinary(length=2048))
    remain_num = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
