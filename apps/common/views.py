# encoding:utf-8
from flask import Blueprint, session, request, render_template, redirect, url_for
from utils.login import make_password, check_password, check_login
from datetime import datetime
from exts import db

bp = Blueprint('common', __name__)


@bp.route('/')
def index():
    return render_template('blog/index.html')
