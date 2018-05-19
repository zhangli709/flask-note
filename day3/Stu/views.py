import random
from flask import Blueprint, render_template, redirect, url_for

from Stu.models import db, Student

# 1.初始化蓝图
blue = Blueprint('stu', __name__)


@blue.route('/')
def index():
    return render_template('index.html')


@blue.route('/scores/')
def scores():
    # 区别django,这里用的是列表，不是字典和元组
    scores_list = [21, 22, 55, 53, 22, 55, 66, 77, 34]
    content_h2 = '<h2>酷酷的</h2>'
    content_h3 = '       <h2>酷酷的</h2>'
    return render_template('scores.html',
                           scores=scores_list,
                           content_h2=content_h2,
                           content_h3=content_h3,
                           )


@blue.route('/createtable/')
def create_db():
    # 数据库创建表，更新到数据库
    db.create_all()
    return '创建成功！'


@blue.route('/droptable/')
def drop_db():
    # 删除数据库里的表
    db.drop_all()
    return '删除成功！'


# 增
@blue.route('/createstu/')
def create_stu():
    # 添加表里的信息
    stu = Student()
    stu.s_name = '小明%d' % random.randrange(1000)
    stu.s_age = '%d' % random.randrange(20)

    # 添加/存储字段到数据库的表里
    db.session.add(stu)
    # 设置回滚方法
    try:
        db.session.commit()
    except:
        db.session.rollback()

    return '创建学生成功'


# 获取全部数据
@blue.route('/stulist/')
def stu_all():
    # 获取数据库里的信息
    stus = Student.query.all()

    return render_template('stulist.html', stus=stus)


# 查询部分数据
@blue.route('/studetail/')
def stu_detail():
    # 1.可以写sql语句，进行原生sql操作
    # sql = 'select * from student where s_name="小明131";'
    # stus = db.session.execute(sql)

    # 2. filter
    # stus = Student.query.filter(Student.s_name == '小明131')

    # 3. filter_by
    stus = Student.query.filter_by(s_name='小明131')

    return render_template('stulist.html', stus=stus)


# 改
@blue.route('/updatestu/')
def update_stu():
    # 第一种方式
    # stu = Student.query.filter_by(s_id=5).first()
    # stu.s_name = '李二狗'

    # 第二种方式
    Student.query.filter_by(s_id=5).update({'s_name': '王大锤'})
    db.session.commit()
    return redirect(url_for('stu.stu_all'))


# 删除
@blue.route('/deletestu/')
def delete_stu():

    stu = Student.query.filter(Student.s_id == 5).first()
    db.session.delete(stu)
    db.session.commit()

    return redirect(url_for('stu.stu_all'))