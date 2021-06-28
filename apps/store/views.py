# encoding:utf-8
from flask import Blueprint, session, request, render_template, redirect, url_for
from .models import StoreUsers
from apps.common.models import CommonUser, Article
from utils.login import make_password, check_password, check_login
from datetime import datetime
from exts import db

bp = Blueprint('store', __name__, url_prefix='/store')


# 前台部分


@bp.route('/')
def index():
    is_login = check_login()
    # if not is_login:
    #     return redirect(url_for('store.login'))
    return render_template('/store/index.html')


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        user = StoreUsers.query.filter_by(username=username).first()
        if user:
            psd = user.password
            if check_password(psd, make_password(password)):
                session['store_username'] = username
                return redirect(url_for('store.index'))
        return render_template('/store/login.html', message='用户名或密码错误')


@bp.route('/logout')
def logout():
    is_login = check_login()
    if is_login:
        session.pop('username')
        session.pop('type')
    return redirect(url_for('store.login'))


@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('/store/register.html')
    else:
        username = request.form.get('username')
        if StoreUsers.query.filter_by(username=username).first():
            return render_template('/store/register.html', message='用户名重复')
        password = request.form.get('password')
        password = make_password(password)
        new_user = StoreUsers(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        session['store_username'] = username
        return redirect(url_for('store.index'))


@bp.route('/product_info')
def product_info():
    message = {
        'p_id': 1,
        'p_name': '测试商品',
        'p_detail': '商品说明商品说明商品说明商品说明商品说明商品说明商品说明商品说明商品说明',
        'p_price': 1223,
        'p_picture_path': '/store/images/produkt_slid1.png'
    }
    return render_template('/store/product_page.html', message=message)


@bp.route('/buy')
def buy():
    p_id = request.args.get('p_id')
    print(p_id)
    return render_template('/store/shopping_cart.html', data=p_id)
