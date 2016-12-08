from app import db


class Student(db.Model):
    # 表名：students
    # 列含义：id，学号， 学生姓名，学生性别，年级，专业id，班级id，层次（本科），学制（4年）
    __tablename__ = 'students'
    id = db.Column(db.Integer(), primary_key=True)
    number = db.Column(db.String(64), index=True, nullable=False, unique=True)
    name = db.Column(db.String(64), index=True, nullable=False)
    sex = db.Column(db.String(64), nullable=False)
    grade = db.Column(db.Integer, nullable=False)
    marjor_id = db.Column(db.Integer, db.ForeignKey('marjors.id'))
    class_id = db.Column(db.Integer, db.ForeignKey('classes.id'))
    level = db.Column(db.String(64), nullable=False, default='本科')
    length_of_schooling = db.Column(db.Integer, nullable=False, default=4)
    scores = db.relationship(
        'Score',
        backref='students',
        lazy='dynamic'
    )

    def __repr__(self):
        return '<Student %r>' % self.name


class Score(db.Model):
    # 表名：scores
    # 列含义：id，学年，学期， 学生id，课程id，原考成绩，补考成绩
    __tablename__ = 'scores'
    id = db.Column(db.Integer(), primary_key=True)
    year = db.Column(db.Integer, nullable=False)
    term = db.Column(db.Integer, nullable=False)
    stu_id = db.Column(db.Integer, db.ForeignKey('students.id'))
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'))
    score1 = db.Column(db.String(64), nullable=False)
    score2 = db.Column(db.String(64), nullable=True)  # 补考成绩可为空

    def __repr__(self):
        return '<Score_id %r>' % self.id


class Major(db.Model):
    # 表名：marjors
    # 列含义：id， 专业名称
    __tablename__ = 'marjors'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(64), nullable=False, index=True)
    students = db.relationship(
        'Student',
        backref='marjors',
        lazy='dynamic'
    )

    def __repr__(self):
        return '<Major %r>' % self.name


class Class(db.Model):
    # 表名：classes
    # 列含义：id，班级名称
    __tablename__ = 'classes'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(64), nullable=False, index=True, unique=True)
    students = db.relationship(
        'Student',
        backref='classes',
        lazy='dynamic'
    )

    def __repr__(self):
        return '<Class %r>' % self.name


class Course(db.Model):
    # 表名：courses
    # 列含义：id，课程名，课程类型
    __tablename__ = 'courses'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(64), nullable=False, index=True)
    category = db.Column(db.String(64), nullable=False)
    power = db.Column(db.Float, nullable=False)
    scores = db.relationship(
        'Score',
        backref='courses',
        lazy='dynamic'
    )

    def __repr__(self):
        return '<Course %r>' % self.name
