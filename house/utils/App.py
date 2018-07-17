#2
from flask import Flask
#3
from App.house_views import house_blueprint
from App.order_views import order_blueprint
from App.user_views import user
from utils.function import init_ext
from utils.settings import template_dir, static_dir, SQLALCHEMY_DATABASE_URI
from utils.config import Config


def create_app():
    app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)
    app.register_blueprint(blueprint=user, url_prefix='/user')
    app.register_blueprint(blueprint=house_blueprint, url_prefix='/house')
    app.register_blueprint(blueprint=order_blueprint, url_prefix='/order')

    # config配置
    app.config.from_object(Config)

    # # 初始化处理包
    init_ext(app)

    return app