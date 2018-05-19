
from flask import Blueprint, render_template

from Grade.models import Grade
from utils.function import db

grade = Blueprint('grade', __name__)


@grade.route('/')
def get_grade():

    return '我是班级'


@grade.route('/createdb/')
def create_db():
    db.create_all()
    return '创建数据表成功'


@grade.route('/dropdb/')
def drop_db():
    db.drop_all()
    return '删除数据表成功'


@grade.route('/creategrade/')
def add_grade():
    names = {'python': '人生',
             'java': 'jaja',
             'html5': 'h5',
             'go': 'gogo'
        }
    grades_list = []
    # for key in names.keys():
    #     grade = Grade(key, names[key])
    #     grades_list.append(grade)

    for key, value in names.items():
        grade = Grade(key, value)
        grades_list.append(grade)
    db.session.add_all(grades_list)
    db.session.commit()

    return '创建班级成功'


# 一对多表的应用，重要
@grade.route('/selectstubygrade/<int:id>/')
def select_stu_by_grade(id):
    grade = Grade.query.get(id)
    stus = grade.students
    return render_template('grade_student.html', stus=stus, grade=grade)


