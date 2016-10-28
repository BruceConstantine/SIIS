from . import main
from flask import render_template


@main.route('/')
def index():
    return 'HelloWorld'


@main.route('/user')
def user():
    return render_template('index.html')
