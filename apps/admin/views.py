# encoding:utf-8
from flask import Blueprint, session, request, render_template, redirect, url_for
from .models import Users
from utils.login import make_password, check_password, check_login
from datetime import datetime
import os, psutil, socket
import platform

bp = Blueprint('admin', __name__, url_prefix='/admin')


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        user = Users.query.filter_by(username=username).first()
        if user:
            psd = user.password
            if check_password(psd, make_password(password)):
                session['username'] = username
                session['type'] = user.type
                return redirect(url_for('admin.index'))
        return render_template('login.html', message='用户名或密码错误')


@bp.route('/index', methods=['GET', 'POST'])
def index():
    is_login = check_login()
    if is_login:
        # print(is_login)
        return render_template('index-2.html', message=is_login)
    else:
        return '未登录'


@bp.route('/welcome')
def welcome():
    is_login = check_login()
    if is_login:
        # info = os.uname()
        is_login['ip'] = request.remote_addr
        with open('utils/start.txt', 'r') as f:
            start = float(f.readline())
            time_now = datetime.now()
            time = datetime.timestamp(time_now)- start
        is_login['sysname'] = platform.platform()
        is_login['nodename'] = socket.gethostname()
        if is_login['type']==1:
            is_login['hostip'] = socket.gethostbyname(socket.gethostname())
            is_login['sysuser'] = psutil.users()[0].name
        boot_start_time = datetime.fromtimestamp(psutil.boot_time())
        boot_time = time_now - boot_start_time
        is_login['boottime'] = str(boot_time).split('.')[0]
        # is_login['release'] = info.release
        # is_login['machine'] = info.machine

        is_login['now'] = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M')
        is_login['time'] = int(time / 60)
        return render_template('welcome.html', message=is_login)


@bp.route('/logout')
def logout():
    is_login = check_login()
    if is_login:
        session.pop('username')
        session.pop('type')
        return redirect(url_for('admin.login'))
    return '未登录'


@bp.route('/add/article')
def add_article():
    is_login = check_login()
    return render_template('article-add.html')


@bp.route('/add/member')
def add_member():
    is_login = check_login()
    return render_template('member-add.html')


@bp.route('/add/picture')
def add_picture():
    is_login = check_login()
    return render_template('picture-add.html')
