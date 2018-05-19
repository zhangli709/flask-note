

# 数据库参数的转换
from flask_sqlalchemy import SQLAlchemy
from flask_debugtoolbar import DebugToolbarExtension
from flask_restful import Api

from flask_marshmallow import Marshmallow

# 初始化
# 数据库
db = SQLAlchemy()
# debug
debugtoolbar = DebugToolbarExtension()
# rest_ful
api = Api()
# marshmallow
ma = Marshmallow()


def get_db_uri(DATABASE):
    # 标准方法转换为自己能用的格式
    user = DATABASE.get('USER', 'root')
    password = DATABASE.get('PASSWORD')
    host = DATABASE.get('HOST')
    port = DATABASE.get('PORT')
    db = DATABASE.get('DB')
    driver = DATABASE.get('DRIVER')
    name = DATABASE.get('NAME')

    return '{}+{}://{}:{}@{}:{}/{}'.format(db, driver,
                                           user, password,
                                           host, port, name)


# 注册
def init_ext(app):
    # 改写原先是SQLAlchemy(app=app)
    db.init_app(app=app)
    # debug
    debugtoolbar.init_app(app=app)
    # rest_ful，返回接口数据
    api.init_app(app=app)
    # marshmallow,配合rest使用，返回筛选过的数据
    ma.init_app(app=app)