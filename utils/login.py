# encoding:utf-8
import hashlib
from flask import session


def make_password(password):
    h = hashlib.md5()
    h.update(password.encode('utf-8'))
    return h.hexdigest()


def check_password(password, psd):
    if psd == password:
        return True
    return False


def check_login():
    username = session.get('username')
    if username:
        return {
            'username': username,
            'type': session.get('type')
        }
    return False


def check_store_login():
    username = session.get('store_username')
    if username:
        return username
    return False

