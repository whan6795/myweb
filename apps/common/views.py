# encoding:utf-8
from flask import Blueprint

bp = Blueprint('common', __name__)


@bp.route('/')
def index():
    return '公共部分首页'
