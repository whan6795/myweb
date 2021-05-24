# encoding:utf-8
from gevent import monkey

monkey.patch_all()
debug = True
loglevel = 'debug'
bind = '127.0.0.1:8080'
pidfile = 'log/gunicorn.pid'
logfile = 'log/debug.log'
workers = 4
worker_class = 'gevent'
