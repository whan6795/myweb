# encoding:utf-8
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask import Flask
from apps.admin import bp as admin_bp
from apps.common import bp as common_bp
from apps.girl import bp as girl_bp
from apps.store import bp as store_bp
from apps.front import bp as front_bp
from exts import db
from utils.login import make_password
from apps.admin import models as admin_models

app = Flask(__name__)
app.register_blueprint(admin_bp)
app.register_blueprint(girl_bp)
app.register_blueprint(store_bp)
app.register_blueprint(common_bp)
app.register_blueprint(front_bp)
app.config.from_object('config')
db.init_app(app)
manager = Manager(app)
Migrate(app, db)
manager.add_command('db', MigrateCommand)


@manager.option('-u', '--username', dest='username')
@manager.option('-p', '--password', dest='password')
@manager.option('-t', '--type', dest='type')  # 1为超级管理员，0为游客
@manager.option('-ln', '--login_num', dest='login_num')
def create_user(username, password, type, login_num):
    user = admin_models.Users(username=username, password=make_password(password), type=type, login_num=login_num)
    db.session.add(user)
    db.session.commit()
    print('添加成功')


@manager.option('-ln', '--login_num', dest='login_num')
def edit_all_user(login_num):
    user = admin_models.Users.query.filter().update({'login_num': login_num})
    # user.login_num = login_num
    db.session.commit()
    print('更改成功')


if __name__ == '__main__':
    manager.run()
