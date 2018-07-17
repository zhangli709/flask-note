#1
import redis
#3
from utils.settings import SQLALCHEMY_DATABASE_URI


class Config():
    # redis配置
    SECRET_KEY = 'secret_key'
    SESSION_TYPE = 'redis'
    SESSION_REDIS = redis.Redis(
        host='47.106.171.59',
        port='6379',
        password='123456'
    )
    SESSION_KEY_PREFIX = 'flask'
    # 绑定mysql配置
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False

