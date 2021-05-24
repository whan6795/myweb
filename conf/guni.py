# encoding:utf-8
from gevent import monkey

monkey.patch_all()
import multiprocessing

debug = True
loglevel = 'debug'
bind = '0.0.0.0:8080'
pidfile = 'log/gunicorn.pid'
logfile = 'log/debug.log'
workers = multiprocessing.cpu_cout() * 2 + 1
worker_class = 'gevent'
