from flask import Blueprint, render_template, request, session, redirect, url_for, make_response
import random

# 1.蓝图初始化
blue = Blueprint('app', __name__)


@blue.route('/')
def hello_world():
    return 'Hello World!'


@blue.route('/login/', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        # 获取存在redis数据库里的session里的值，返回页面
        username = session.get('username')
        return render_template('login.html', username=username)
    if request.method == 'POST':
        # 获取网页里的值，存在redis的session里。
        username = request.form.get('username')
        session['username'] = username
        return redirect(url_for('app.login'))


@blue.route('/getresponse/')
def get_response():
    # 存储cookie
    response = make_response('<h2>你是大帅逼</h2>')
    ticket = ''
    s = 'abcdefghijklmnopqrstuvwxyz0123456789'
    for i in range(20):
        ticket += random.choice(s)
    response.set_cookie('ticket', ticket, max_age='', expires='')
    return response


@blue.route('/deletecookie/')
def del_cookie():
    # 删除cookie
    response = make_response('<h2>你是大帅逼</h2>')
    response.delete_cookie('ticket')
    return response