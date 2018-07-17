#1
import os

from utils.function import transfer_mysql

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
template_dir = os.path.join(BASE_DIR, 'templates')
static_dir = os.path.join(BASE_DIR, 'static')

DATABASE = {
    # 用户
    'USER': 'root',
    # 密码
    'PASSWORD': '123456',
    # 地址
    'HOST': 'localhost',
    # 端口
    'PORT': '3306',
    # 数据库名称
    'NAME': 'flask_house',
    # 数据库
    'DB': 'mysql',
    # 驱动
    'DRIVER': 'pymysql',
}

SQLALCHEMY_DATABASE_URI = transfer_mysql(DATABASE)

# 配置上传文件的路径
UPLOAD_DIRS = os.path.join(os.path.join(BASE_DIR, 'static'), 'upload')