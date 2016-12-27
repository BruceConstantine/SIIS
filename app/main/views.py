from flask import render_template, request, jsonify
from . import main
from app.models import Student, Major, Class


@main.route('/index')
@main.route('/')
def index():
    stu = Student.query.all()
    marjor = Major.query.all()
    _class = Class.query.all()
    return render_template(
        'index.html',
        count_stu=len(stu),
        count_marjor=len(marjor),
        count_class=len(_class))


@main.route('/login')
def login():
    return render_template("login.html")


@main.route('/register')
def register():
    return render_template("register.html")


@main.route('/student')
def student():
    return render_template("student.html")


@main.route('/student_info')
def stu_info():
    stu_num = request.args['student_number']
    print(stu_num)
    this_student = Student.query.filter_by(number=stu_num).first()
    if this_student:
        return jsonify({
            'number': this_student.number,
            'name': this_student.name,
            'sex': this_student.sex,
            'grade': this_student.grade,
            'marjor': this_student.marjors.name,
            'class': this_student.classes.name,
            'level': this_student.level,
            'length_of_schooling': this_student.length_of_schooling
        })
    else:
        return jsonify({
            'number': 'none',
            'name': 'none',
            'sex': 'none',
            'grade': 'none',
            'marjor': 'none',
            'class': 'none',
            'level': 'none',
            'length_of_schooling': 'none'
        })


@main.route('/theme')
def theme():
    return render_template("theme.html")
