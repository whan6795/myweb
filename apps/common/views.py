# encoding:utf-8
from flask import Blueprint, session, request, render_template, redirect, url_for
from utils.login import make_password, check_password, check_login
from datetime import datetime
from apps.common.models import CommonUser, Article
from exts import db

bp = Blueprint('common', __name__)


@bp.route('/')
def index():
    # 每页3个，查询第2页的数据
    # paginate = User.query.paginate(page, per_page, Error_out)
    # paginate = User.query.paginate(2, 3, False)
    # page: 哪一个页
    # per_page: 每页多少条数据
    # Error_out: False
    # 查不到不报错
    #
    # pages: 共有多少页
    # items: 当前页数的所有对象
    # page: 当前页
    page = int(request.args.get('page', 1))  # 当前页数
    per_page = int(request.args.get('page_num', 5))  # 设置每页数量
    paginate = Article.query.filter_by(status=1).order_by(Article.id).paginate(page, per_page, error_out=False)
    article_list = paginate.items
    message = {
        'page': page,
        'paginate': paginate,
        'articles': []
    }
    for i in article_list:
        message['articles'].append(
            {
                'title': i.title,
                'content': i.content[100] if len(i.content) > 100 else i.content,
                'id': i.id
            }
        )
    print(message)
    return render_template('blog/index.html', message=message)


@bp.route('/article/<int:id>')
def getArticle(id):
    article = Article.query.filter_by(id=id).first()
    if article.status:
        message = {}
        message['title'] = article.title
        message['content'] = article.content
        return render_template('blog/article.html', message=message)
    else:
        return redirect(url_for('common.index'))
