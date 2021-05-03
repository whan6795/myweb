# encoding:utf-8
DEBUG = True
from flask import Flask
from apps.admin import bp as admin_bp
from apps.common import bp as common_bp
from apps.front import bp as front_bp
from exts import db
from flask_wtf import CSRFProtect

def create_app():
    app = Flask(__name__)
    app.register_blueprint(admin_bp)
    app.register_blueprint(common_bp)
    app.register_blueprint(front_bp)
    app.config.from_object('config')
    CSRFProtect(app)
    db.init_app(app)
    return app


# @app.route('/')
# def hello_world():
#     return 'hello world'


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port='8080')
