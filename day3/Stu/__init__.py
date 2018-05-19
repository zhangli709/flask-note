import redis
from flask import Flask, Session
from flask_sqlalchemy import SQLAlchemy
import os

from Stu.views import blue


def create_app():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    template_dir = os.path.join(BASE_DIR, 'templates')
    static_dir = os.path.join(BASE_DIR, 'static')
    app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)
    # 2.注册蓝图
    app.register_blueprint(blueprint=blue, url_prefix='/stu')

    # 连接数据库redis
    # app.config['SECRET_KEY'] = 'secret_key'
    # app.config['SESSION_TYPE'] = 'redis'
    # app.config['SESSION_REDIS'] = redis.Redis(
    #     host='127.0.0.1',
    #     port='6379'
    # )
    # app.config['SESSION_KEY_PREFIX'] = 'flask'
    # Session(app)

    # 连接数据库mysql,初始化,配置
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost:3306/flask3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    SQLAlchemy(app=app)

    return app