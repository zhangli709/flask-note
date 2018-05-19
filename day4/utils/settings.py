
import os

from utils.function import get_db_uri


# 基础路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 页面模板
template_dir = os.path.join(BASE_DIR, 'templates')
# 静态模板
static_dir = os.path.join(BASE_DIR, 'static')

# 仿照django配置连接数据库的方式
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
    'NAME': 'flask3',
    # 数据库
    'DB': 'mysql',
    # 驱动
    'DRIVER': 'pymysql',
}

# 连接数据库，调用方法，将国际方法改为自己的连接方式
SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)