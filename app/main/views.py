from flask import render_template
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


@main.route('/theme')
def theme():
    return render_template("theme.html")
