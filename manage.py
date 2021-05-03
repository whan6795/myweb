# encoding:utf-8
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import create_app
from exts import db,make_password
from apps.admin import models as admin_models

app = create_app()
manager = Manager(app)
Migrate(app, db)
manager.add_command('db', MigrateCommand)


@manager.option('-u', '--username', dest='username')
@manager.option('-p', '--password', dest='password')
@manager.option('-t', '--type', dest='type')
def create_user(username, password, type):
    user = admin_models.Users(username=username, password=make_password(password), type=type)
    db.session.add(user)
    db.session.commit()
    print('添加成功')


if __name__ == '__main__':
    manager.run()
