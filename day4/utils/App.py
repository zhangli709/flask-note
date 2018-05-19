from flask import Flask


from Grade.views import grade
from Stu.views import blue
from utils.function import init_ext
from utils.settings import template_dir, static_dir, SQLALCHEMY_DATABASE_URI


def create_app():
    # 初始化app，绑定蓝图，前缀
    app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

    app.debug = True
    app.config['SECRET_KEY'] = 'secret_key'

    app.register_blueprint(blueprint=blue, url_prefix='/stu')
    app.register_blueprint(blueprint=grade, url_prefix='/grade')
    # 连接数据库
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # 导入方式
    init_ext(app)
    return app