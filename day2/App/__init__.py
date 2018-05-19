
import os
from flask import Flask
from flask_session import Session
import redis
from App.views import blue


def create_app():
    # 配置网页和静态资源的路径
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    static_dir = os.path.join(BASE_DIR, 'static')
    template_dir = os.path.join(BASE_DIR, 'templates')
    # 初始化路径
    app = Flask(__name__, static_folder=static_dir, template_folder=template_dir)
    # 2.蓝图注册 ,前缀名最好和蓝图名字一样。
    app.register_blueprint(blueprint=blue, url_prefix='/app')

    # 密钥
    app.config['SECRET_KEY'] = 'secret_key'
    # 使用redis存储信息,默认访问redis,127.0.0.1:6379
    app.config['SESSION_TYPE'] = 'redis'
    # 连接任意id的redis
    app.config['SESSION_REDIS'] = redis.Redis(host='127.0.0.1', port='6379')
    # 定义前缀,在密码的前面加上如下前缀
    app.config['SESSION_KEY_PREFIX'] = 'flask'


    # 第一种方式，初始化app
    Session(app)
    # 第二种方式，初始化app
    # se = Session()
    # se.init_app(app)
    return app