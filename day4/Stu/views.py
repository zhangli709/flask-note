from flask import Blueprint, render_template, request, redirect, url_for
from sqlalchemy import and_, or_, not_

from Stu.models import Student, Course, sc
from Stu.stuMarshmallow import stumarsh
from utils.function import db, api


from flask_restful import Resource


blue = Blueprint('stu', __name__)


@blue.route('/')
def hello_world():
    return 'Hello World!'


@blue.route('/index/')
def index():
    return render_template('index.html')


@blue.route('/createdb/')
def create_db():
    db.create_all()
    return '创建数据表成功'


@blue.route('/dropdb/')
def drop_db():
    db.drop_all()
    return '删除数据表成功'


# 创建单个学生
@blue.route('/createstu/', methods=['POST', 'GET'])
def create_stu():
    if request.method == 'GET':
        return render_template('create_stu.html')
    if request.method == 'POST':
        username = request.form.get('username')
        age = request.form.get('age')

        stu1 = Student(username, age)
        db.session.add(stu1)
        try:
            db.session.commit()
        except:
            db.session.rollback()

        return '添加成功'


#一次创建多个学生
@blue.route('/createstus/', methods=['GET', 'POST'])
def create_stus():
    if request.method == 'GET':
        return render_template('create_stus.html')
    if request.method == 'POST':
        stus_list = []
        username1 = request.form.get('username1')
        age1 = request.form.get('age1')

        username2 = request.form.get('username2')
        age2 = request.form.get('age2')

        stu1 = Student(username1, age1)
        stu2 = Student(username2, age2)

        # 一次传入多个信息，把这些信息存储到列表里，然后add_all提交列表
        stus_list.append(stu1)
        stus_list.append(stu2)
        db.session.add_all(stus_list)
        db.session.commit()

        return '创建多个学生成功'


# 查询进阶
@blue.route('/selectstu/')
def select_stu():
    # 年龄小于16岁的学生的信息 le <=  lt <
    # stus = Student.query.filter(Student.s_age < 16)
    # stus = Student.query.filter(Student.s_age.__lt__(16))

    # 年龄大于10岁的学生 gt >  ge >=
    # stus = Student.query.filter(Student.s_age.__gt__(12))

    # 年龄在范围内的 in_
    # stus = Student.query.filter(Student.s_age.in_([13, 14]))

    # sql语句查询
    # sql = 'select * from d4student;'
    # stus = db.session.execute(sql)

    #按照id排列
    # stus = Student.query.order_by('s_id')

    # 按照id降序排列，获取前三个
    # stus = Student.query.order_by('s_id').limit(3)

    # 获取年龄最大的一个
    # stus = Student.query.order_by('-s_age').first()

    # 跳过1个数据，查询1个信息
    # stus = Student.query.order_by('-s_age').offset(1).limit(1)

    #** 获取id等于1的学生, filter and get diff
    # stus = Student.query.filter(Student.s_id == 1)

    # stus = Student.query.get(24)

    # 单表多条件查询
    # stus = Student.query.filter(Student.s_age==11, Student.s_name=='火神')

    # and_
    # stus = Student.query.filter(and_(Student.s_age == 11, Student.s_name == '火神'))

    # or_
    # stus = Student.query.filter(or_(Student.s_age == 13, Student.s_name == '火神'))

    # not_
    stus = Student.query.filter(not_(Student.s_name == '火神'))

    return render_template('student_list.html', stus=stus)


@blue.route('/stupage/')
def stu_page():
    # 分页操作
    # 当前第一页
    page = int(request.args.get('page', 1))
    # 每页多少条数据
    perpage = int(request.args.get('per_page', 3))
    # 所有数据实例化
    paginate = Student.query.order_by('-s_id').paginate(page, perpage, error_out=False)

    # 当前页面的总信息
    stus = paginate.items

    return render_template('paginate.html', paginate=paginate, stus=stus)


# 一对多 ，表的应用，
@blue.route('/selectgradebystu/<int:id>/')
def select_grade_by_stu(id):
    stu = Student.query.get(id)
    grade = stu.stu
    return render_template('grade_to_student.html', grade=grade, stu=stu)


# 给课程表假数据
@blue.route('/addcourse/')
def add_course():
    courses = ['语文','数学', '英语', '体育', '物理', '化学', '生物']
    course_list = []
    for course in courses:
        cou = Course(course)
        course_list.append(cou)
    db.session.add_all(course_list)
    db.session.commit()

    return '添加课程成功'


@blue.route('/stucourse/', methods=['POST', 'GET'])
def stu_cou():
    if request.method == 'GET':
        stus = Student.query.all()
        cous = Course.query.all()
        return render_template('stu_cou.html', stus=stus, cous=cous)
    if request.method == 'POST':
        s_id = request.form.get('student')
        c_id = request.form.get('course')
        # sql 语句存值 方法一
        # sql = 'insert into sc(s_id,c_id) value (%s, %s);' % (s_id, c_id)
        # db.session.execute(sql)
        # db.session.commit()

        # 方法二
        stu = Student.query.get(s_id)
        cou = Course.query.get(c_id)

        # append操作，记住吧，添加中间表的方法，
        # cou.students.append(stu)
        stu.cou.append(cou)
        db.session.add(stu)
        db.session.commit()

        return 'sc添加成功'


# 批量添加中间表的信息
@blue.route('/stucourseall/', methods=['POST', 'GET'])
def stu_cou_all():
    if request.method == 'GET':
        stus = Student.query.all()
        cous = Course.query.all()
        return render_template('stu_cou.html', stus=stus, cous=cous)
    if request.method == 'POST':
        # s_id = request.form.get('student')
        # c_id1 = request.form.get('course1')
        # c_id2 = request.form.get('course2')
        # c_id3 = request.form.get('course3')
        # c_id4 = request.form.get('course4')
        #
        # stu = Student.query.get(s_id)
        # cou1 = Course.query.get(c_id1)
        # cou2 = Course.query.get(c_id2)
        # cou3 = Course.query.get(c_id3)
        # cou4 = Course.query.get(c_id4)
        #
        # cou_list =[cou1, cou3, cou2,cou4]
        # for cou in cou_list:
        #     stu.cou.append(cou)
        #
        # db.session.add_all(cou_list)
        # db.session.commit()

        s_id = request.form.get('student')
        c_ids = request.form.getlist('course')
        stu = Student.query.get(s_id)
        for c_id in c_ids:
            cou = Course.query.get(c_id)
            cou.students.append(stu)
            db.session.add(cou)
        db.session.commit()

        return 'sc多个信息添加成功'


#信息展示
@blue.route('/allstu/')
def all_stu():
    stus = Student.query.all()

    return render_template('all_stu.html', stus=stus)


# 连接上面方法，展示信息
@blue.route('/selectcoubystu/<int:id>/')
def select_cou_by_stu(id):
    stu = Student.query.get(id)
    cous = stu.cou

    return render_template('stucourse.html', cous=cous, stu=stu)



#连接上面的方法，删除学生对应的课程
@blue.route('/deletecoubystu/<int:sid>/<int:cid>/')
def delete_cou_by_stu(sid,cid):
    stu = Student.query.get(sid)
    cou = Course.query.get(cid)
    # sql
    # sql = 'delete from sc where s_id =%s and c_id= %s;' % (sid, cid)
    # db.session.execute(sql)
    # db.session.commit()
    # 常规方法, remove
    cou.students.remove(stu)
    db.session.commit()
    return redirect(url_for('stu.all_stu'))





# rest_ful, 区别于其他的，是定义的类，专门用来写接口的,restful
class HelloStudent(Resource):

    def get(self, id):

        stu = Student.query.get(id)
        return stumarsh.jsonify(stu)

    def post(self, id):

        pass

    def patch(self):

        pass

    def put(self):

        pass

    def delete(self):

        pass


api.add_resource(HelloStudent, '/api/hello/<int:id>/')