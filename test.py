# encoding:utf-8
from exts import check_password,make_password
import hashlib
password='123456'
psd_hash = make_password(password)
psd_input = make_password(password)
print(psd_hash,check_password(psd_input,psd_hash))