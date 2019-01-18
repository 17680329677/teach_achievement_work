from app import create_app, db
from flask_script import Manager, Shell
from app.models import Teacher
import os
import sys
import click

COV = None
if os.environ.get('FLASK_COVERAGE'):
    import coverage
    COV = coverage.coverage(branch=True, include='app/*')
    COV.start()


app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)


def make_shell_context():
    return dict(app=app, db=db, Teacher=Teacher)


if __name__ == '__main__':
    manager.run()
    app.run(debug=True)
