# encoding:utf-8
from exts import db
from datetime import datetime


class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50), nullable=False)
    type = db.Column(db.Integer, nullable=False)  # 文章类型，0代表...1代表...
    status = db.Column(db.Boolean)  # 0不可见，1可见
    content = db.Column(db.Text)
    comments = db.Column(db.Boolean)  # 0不允许评论，1允许评论
    author_id = db.Column(db.Integer)


class CommonUser(db.Model):  # 网站用户
    __tablename__ = 'common_user'
    uid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(50), nullable=False)
