# encoding:utf-8
DEBUG = True
from flask import Flask
from apps.admin import bp as admin_bp
from apps.common import bp as common_bp
from apps.girl import bp as girl_bp
from apps.store import bp as store_bp
from apps.front import bp as front_bp
from exts import db
from flask_wtf import CSRFProtect
from datetime import datetime

app = Flask(__name__)
app.register_blueprint(admin_bp)
app.register_blueprint(girl_bp)
app.register_blueprint(store_bp)
app.register_blueprint(common_bp)
app.register_blueprint(front_bp)
app.config.from_object('config')
CSRFProtect(app)
db.init_app(app)

# @app.route('/')
# def hello_world():
#     return 'hello world'


if __name__ == '__main__':
    with open('utils/start.txt', 'w') as f:
        f.write(str(datetime.timestamp(datetime.now())))
    app.run(debug=True, host='0.0.0.0', port='8080', threaded=True)  # , host='0.0.0.0', port='8080'
