from app import create_app, db
from flask_script import Manager, Shell
from flask_migrate import MigrateCommand, Migrate
from spider import xhcx, zcjcx
from app.models import Student, Score, Major, Class, Course

app = create_app('default')
manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(
        app=app,
        db=db,
        Student=Student,
        Score=Score,
        Major=Major,
        Class=Class,
        Course=Course
    )


@manager.command
def hello():
    # print('HelloWorld %s' % stu_number)
    # xhcx.parse(xhcx.splider('1411'))
    xhcx.parse(response=xhcx.splider('1411'), year='1411')
    # xhcx.splider('1411')


@manager.command
def test():
    xhcx.test()


manager.add_command('db', MigrateCommand)
manager.add_command('shell', Shell(make_context=make_shell_context))

if __name__ == '__main__':
    manager.run()
