
#2
import functools

from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import redirect

db = SQLAlchemy()
session = Session()


def transfer_mysql(DATABASE):
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


def init_ext(app):
    db.init_app(app=app)
    session.init_app(app)


# 登录验证的装饰器
def is_login(view_fun):
    @functools.wraps(view_fun)
    def decorator():
        try:
            # 验证用户是否登录，即session里是否有值。
            if 'user_id' in session:
                return view_fun
            else:
                return redirect('/user/login/')
        except:
            return redirect('/user/login/')

    return decorator