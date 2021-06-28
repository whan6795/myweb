# encoding:utf-8
from flask import Blueprint, session, request, render_template, redirect, url_for
from .models import StoreUsers, Commodity
from utils.login import *
from datetime import datetime
from exts import db

bp = Blueprint('store', __name__, url_prefix='/store')


# 前台部分


@bp.route('/')
def index():
    is_login = check_store_login()
    if not is_login:
        return redirect(url_for('store.login'))
    commodities = Commodity.query.all()
    re = []
    for commodity in commodities:
        data = {
            'id': commodity.uid,
            'picture': commodity.picture,
            'name': commodity.name,
            'price': commodity.price
        }
        re.append(data)

    return render_template('/store/index.html', data=re)


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('store/login.html')
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
    is_login = check_store_login()
    if is_login:
        session.pop('store_username')
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
        new_user = StoreUsers(username=username, password=password, money=500)
        db.session.add(new_user)
        db.session.commit()
        session['store_username'] = username
        return redirect(url_for('store.index'))


@bp.route('/product_info')
def product_info():
    is_login = check_store_login()
    if not is_login:
        return redirect(url_for('store.login'))
    p_id = request.args.get('p_id')
    print(p_id)
    commodity = Commodity.query.filter_by(uid=p_id).first()
    message = {
        'p_id': commodity.uid,
        'p_name': commodity.name,
        'p_detail': commodity.detail,
        'p_price': commodity.price,
        'p_picture_path': commodity.picture if commodity.picture else '/store/images/null_picture.jpg'
    }
    return render_template('/store/product_page.html', message=message)


@bp.route('/buy')
def buy():
    is_login = check_store_login()
    if not is_login:
        return redirect(url_for('store.login'))
    s_user = StoreUsers.query.filter_by(username=is_login).first()
    p_id = request.args.get('p_id')
    commodity = Commodity.query.filter_by(uid=p_id).first()
    message = {
        'done_or_not': 'not',
        'p_id': commodity.uid,
        'p_name': commodity.name,
        'p_detail': commodity.detail,
        'p_price': commodity.price,
        'p_picture_path': commodity.picture if commodity.picture else '/store/images/null_picture.jpg',
        'remain_money': s_user.money
    }
    return render_template('/store/shopping_cart.html', message=message)


@bp.route('/done')
def buy_done():
    is_login = check_store_login()
    if not is_login:
        return redirect(url_for('store.login'))
    s_user = StoreUsers.query.filter_by(username=is_login).first()
    price = int(request.args.get('price'))
    s_money = int(s_user.money)
    if s_money >= price:
        s_user.money = str(s_money - price)
        db.session.commit()
        message = {
            'done_or_not': 'done',
            'remain_money': s_user.money
        }
    else:
        message = {'done_or_not': 'no_enough_money', 'remain_money': s_user.money, 'price': price}
    return render_template('/store/shopping_cart.html', message=message)
