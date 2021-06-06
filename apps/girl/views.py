# encoding:utf-8
from flask import Blueprint

bp = Blueprint('girl', __name__, url_prefix='/mygirl')


@bp.route('/')
def index():
    return '女友blog首页'
