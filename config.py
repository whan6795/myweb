# encoding:utf-8
from datetime import timedelta

CSRF_ENABLED = True
SECRET_KEY = 'wh971220'

# flask-sqlalchemy配置
DIALECT = 'mysql'
DRIVER = 'pymysql'
USERNAME = 'ubuntu'
PASSWORD = 'wh001108'
PORT = '3306'
HOST = '127.0.0.1'
DATABASE = 'myweb'
SQLALCHEMY_DATABASE_URI = '{}+{}://{}:{}@{}:{}/{}?charset=utf8'.format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT,
                                                                       DATABASE)
SQLALCHEMY_TRACK_MODIFICATIONS = False  # 关闭动态跟踪
SQLALCHEMY_ECHO = True  # 查询时显示原始sql语句


