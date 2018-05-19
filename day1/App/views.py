import uuid

from flask import send_file, request, make_response, render_template, redirect, url_for, abort

from flask import Blueprint

# 1. 初始化，first,蓝图的名字
blue = Blueprint('first', __name__)


# 路由（127.0.0.1:5000)
@blue.route('/', methods=['POST', 'GET'])
def hello_world():
    # 视图函数
    return 'Hello World!'


@blue.route('/hello/<name>/', methods=['POST','GET'])
def hello_man(name):
    print(type(name))
    return 'hello name:%s type:%s' % (name, type(name))


@blue.route('/helloint/<int:id>/')
def hello_int(id):
    print(id)
    print(type(id))
    return 'hello int:%s' % id


@blue.route('/index/')
def index():
    # return render_template('hello.html')
    return send_file('../templates/hello.html')


@blue.route('/getfloat/<float:price>/')
def hello_float(price):

    return 'float:%.2f' % price


@blue.route('/getstr/<string:str>/')
def hello_str(str):
    return 'str:%s' % str


# 这里的path可以时任意东西
@blue.route('/getpath/<path:url_path>/')
def hello_path(url_path):
    return 'path:%s' % url_path


@blue.route('/getuuid/')
def hello_get_uuid():
    a=uuid.uuid4()
    return str(a)


@blue.route('/getbyuuid/<uuid:uu>/')
def hello_uuid(uu):
    return 'uuid:%s' % uu


@blue.route('/getrequest/', methods=['GET', 'POST'])
def get_request():
    args = request.args
    form = request.form
    return '获取request'


# 响应
@blue.route('/makeresponse/')
def make_responses():
    # response = make_response('<h2>标题</h2>')
    a = render_template('hello.html')
    response = make_response(a, 250)  # 状态码，响应
    return response


# 跳转
@blue.route('/redirect/')
def make_redirect():
    # 地址跳转1,url
    # return redirect('/hello/index/')
    # 2,蓝图名和方法名，效果同上
    return redirect(url_for('first.index'))


# 异常演示
@blue.route('makeabort')
def make_abort():
    abort(400)
    return '终结'


#捕捉异常
@blue.errorhandler(404)
def get_error(exception):
    return '捕捉异常：%s' % exception


