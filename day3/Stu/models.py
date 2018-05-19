
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Student(db.Model):
    # ID主键，自增，整数
    s_id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    s_name = db.Column(db.String(20), unique=True)
    s_age = db.Column(db.INTEGER, default=18)

    __tablename__ = 'student'