#1
from flask import Flask
import os
#3
from App.views import blue


def create_app():
    # 手动添加templates static 的路径。
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    templates_dir = os.path.join(BASE_DIR, 'templates')
    static_dir = os.path.join(BASE_DIR, 'static')
    app = Flask(__name__, static_folder=static_dir, template_folder=templates_dir)  # 初始化
    # 2. 注册路由
    app.register_blueprint(blueprint=blue, url_prefix='/hello')  # 给蓝图加个名字区别

    return app
