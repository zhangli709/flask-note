from utils.function import db


class Student(db.Model):
    s_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    s_name = db.Column(db.String(20), unique=True)
    s_age = db.Column(db.Integer, default=18)
    # 连接外键1,一定要表名加字段
    s_g = db.Column(db.Integer, db.ForeignKey('d4grade.g_id'), nullable=True)

    __tablename__ = 'd4student'

    def __init__(self, name, age):
        """
        初始化方法，给一个函数，方便给表内容赋值
        :param name:
        :param age:
        """
        self.s_name = name
        self.s_age = age


# 中间关联表，把student course 关联起来
sc = db.Table('sc',
              db.Column('s_id', db.Integer, db.ForeignKey('d4student.s_id')),
              db.Column('c_id', db.Integer, db.ForeignKey('course.c_id'))
              )


class Course(db.Model):
    c_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    c_name = db.Column(db.String(10), unique=True)
    students = db.relationship('Student', secondary=sc, backref='cou')

    # __tablename__ = 'course'
    def __init__(self, name):
        self.c_name = name
