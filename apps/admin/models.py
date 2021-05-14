# encoding:utf-8
from exts import db
from datetime import datetime


class Users(db.Model):  # 后台用户（1超管0游客）
    __tablename__ = 'user'
    uid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(50), nullable=False)
    type = db.Column(db.Integer, nullable=False)
    login_num = db.Column(db.Integer, default=0)
    last_login_time = db.Column(db.DateTime)
    login_time = db.Column(db.DateTime)
