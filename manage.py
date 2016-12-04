from app import create_app, db
from flask_script import Manager, Shell
from flask_migrate import MigrateCommand, Migrate
from spider import xhcx, zcjcx

app = create_app('default')
manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(app=app, db=db)


@manager.command
def hello(stu_number):
    print('HelloWorld %s' % stu_number)
    xhcx.parse(xhcx.splider('1411'))


manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
