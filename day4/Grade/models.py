from _datetime import datetime

from utils.function import db


class Grade(db.Model):

    g_id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    g_name = db.Column(db.String(10), unique=True)
    g_desc = db.Column(db.String(100), nullable=True)
    g_time = db.Column(db.Date, default=datetime.now())
    # 外键关联2,只能是Student,类名
    students = db.relationship('Student', backref='stu', lazy=True)
    # lazy 懒加载，调用它，才查询他，否则部查询
    __tablename__ = 'd4grade'

    def __init__(self, name, desc):
        self.g_name = name
        self.g_desc = desc
