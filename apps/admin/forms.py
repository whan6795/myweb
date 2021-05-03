# encoding:utf-8
from wtforms import Form
from wtforms import StringField, BooleanField
from wtforms.validators import InputRequired, Length


class LoginForm(Form):
    username = StringField(
        label='用户名',
        validators=[
            InputRequired('用户名为必填项'),
            Length(2, 20, '用户名长度为2-20')
        ]
    )
    password = StringField(
        label='密码',
        validators=[
            InputRequired('密码为必填项'),
            Length(6, 12, '密码长度为6-12位')
        ]
    )
