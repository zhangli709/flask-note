#1
import re
#2
import os
from flask import Blueprint, request, render_template, redirect, jsonify, session
#3
from App.models import db, User
from utils.function import is_login
from utils.settings import UPLOAD_DIRS

from utils.status_code import USER_REGISTER_PARAMS_ERROR, USER_REGISTER_MOBILE_ERROR, USER_REGISTER_MOBILE_IS_EXSITS, \
    USER_REGISTER_PASSWORD_NOT_EQUAL, DATABASE_ERROR, SUCCESS, PARAMS_ERROR, USER_LOGIN_IS_NOT_EXSIST, \
    USER_LOGIN_PASSWORD_IS_ERROR, USER_UPLOAD_IMAGE_IS_ERROR, USER_LOGIN_IS_EXSIST, USER_ID_IS_EXSIST, OK

user = Blueprint('user', __name__)


@is_login
@user.route('/createdb/')
def create_db():
    db.create_all()
    return '数据库表创建成功'


@is_login
@user.route('/dropdb/')
def drop_db():
    db.drop_all()
    return '你该跑路了！数据库已经删除'


@user.route('/regist/', methods=['GET'])
def regist():
    return render_template('register.html')


@user.route('/regist/', methods=['POST'])
def regist_message():

    # 从页面获取值
    register_dict = request.form
    mobile = register_dict.get('mobile')
    password = register_dict.get('password')
    password2 = register_dict.get('password2')

    # 经过判断之后，再决定是否保存到数据库里
    # 判断是否为空
    if not all([mobile, password, password2]):
        return jsonify(USER_REGISTER_PARAMS_ERROR)
    # 正则判断手机号
    if not re.match(r'^1[34578]\d{9}$', mobile):
        return jsonify(USER_REGISTER_MOBILE_ERROR)

    # 手机号是否被注册
    if User.query.filter(User.phone == mobile).count():
        return jsonify(USER_REGISTER_MOBILE_IS_EXSITS)

    if password != password2:
        return jsonify(USER_REGISTER_PASSWORD_NOT_EQUAL)

    # 实例化一个对象
    user = User()
    user.phone = mobile
    user.password = password
    user.name = mobile

    # 保存数据到数据库
    try:
        user.add_update()
        return jsonify(SUCCESS)
    except:
        return jsonify(DATABASE_ERROR)


@user.route('/login/', methods=['GET'])
def login():
    return render_template('login.html')


@user.route('/login/', methods=['POST'])
def user_login():
    user_dict = request.form
    mobile = user_dict.get('mobile')
    password = user_dict.get('password')

    # 判断是否为空
    if not all([mobile, password]):
        return jsonify(PARAMS_ERROR)

    # 判断是否手机号符合规则
    if not re.match(r'^1[34578]\d{9}$', mobile):
        return jsonify(USER_REGISTER_MOBILE_ERROR)

    # 验证用户名和密码，并将用户信息存在redis里。
    user = User.query.filter(User.phone==mobile).first()
    if user:
        if user.check_pwd(password):
            # 用户信息存在session,和cookie一样，在页面里，可以随时调用
            session['user_id'] = user.id
            return jsonify(SUCCESS)
        else:
            return jsonify(USER_LOGIN_PASSWORD_IS_ERROR)
    else:
        return jsonify(USER_LOGIN_IS_NOT_EXSIST)


@is_login
@user.route('/logout/', methods=['GET'])
def logout():
    # 删除session里的值
    session.clear()
    return jsonify(SUCCESS)


@is_login
@user.route('/my/', methods=['GET'])
def my():

    return render_template('my.html')


# 页面加载完成，就偷偷的请求这个方法，将用户信息拿到，并且通过ajax方法，把他渲染出来，my.html的页面
@is_login
@user.route('/user/', methods=['GET'])
def get_user_profile():
    user_id = session['user_id']
    user = User.query.get(user_id)

    # 调用models里定义的to_basic_dict方法，将<User> 转换为json字典格式
    return jsonify(user=user.to_basic_dict(), code=OK)


# 个人信息页面

@user.route('/profile/', methods=['GET'])
def profile():
    return render_template('profile.html')


# 个人信息页面，上传头像和用户名到数据库
@is_login
@user.route('/profile/', methods=['PUT'])
def user_profile():
    user_dict = request.form
    file_dict = request.files
    # 判断是否为空
    if 'avatar' in file_dict:
        # 获取要上传文件的路径
        f1 = file_dict['avatar']
        # mimetype 上传文件的类型
        if not re.match(r'^image/.*$', f1.mimetype):
            return jsonify(USER_UPLOAD_IMAGE_IS_ERROR)

        # url = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        # url = os.path.join(url, 'static')
        # url = os.path.join(url, 'upload')
        # url = os.path.join(url, f1.filename)
        # 修改存储位置到settings里面,引用配置, 将上传的文件保存在UPLOAD_DIRS目录下，使用f1.filename名字
        url = os.path.join(UPLOAD_DIRS, f1.filename)
        f1.save(url)

        # 在数据库里保存相对路径
        user = User.query.filter(User.id == session['user_id']).first()
        # 相对路径，保存到数据库里
        image_url = os.path.join('/static/upload/', f1.filename)
        user.avatar = image_url

        try:
            user.add_update()
            return jsonify(code=OK, url=image_url)
        except Exception as e:
            return jsonify(DATABASE_ERROR)

    elif 'name' in user_dict:

        name = user_dict.get('name')
        if User.query.filter(User.name == name).count():
            return jsonify(USER_LOGIN_IS_EXSIST)
        user = User.query.get(session['user_id'])
        user.name = name
        try:
            user.add_update()
            return jsonify(SUCCESS)
        except Exception as e:
            return jsonify(DATABASE_ERROR)

    else:
        return jsonify(PARAMS_ERROR)


# 实名认证
@is_login
@user.route('/auth/', methods=['GET'])
def auth():
    return render_template('auth.html')


# 从数据库里获取当前用户实名认证的信息
@is_login
@user.route('/auths/', methods=['GET'])
def get_user_auth():
    user = User.query.get(session['user_id'])

    return jsonify(code='200',
                   id_name=user.id_name,
                   id_card=user.id_card)


# 上传实名认证的信息到数据库
@is_login
@user.route('/auths/', methods=['PUT'])
def user_auth():
    id_name = request.form['id_name']
    id_card = request.form['id_card']
    # 判断是否为空
    if not all([id_name, id_card]):
        return jsonify(PARAMS_ERROR)

    # 判断是否省份证符合规则
    if not re.match(r'^[1-9]\d{5}(18|19|([23]\d))\d{2}((0[1-9])|(10|11|12))(([0-2][1-9])|10|20|30|31)\d{3}[0-9Xx]$', id_card):
        return jsonify(PARAMS_ERROR)
    # 判断是否被使用
    if User.query.filter(User.id_card == id_card).count():
        return jsonify(USER_ID_IS_EXSIST)
    else:
        try:
            user = User.query.get(session['user_id'])
            user.id_card = id_card
            user.id_name = id_name
            user.add_update()
            return jsonify(SUCCESS)
        except Exception:
            return jsonify(DATABASE_ERROR)
