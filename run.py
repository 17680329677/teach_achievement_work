from app import app
from flask_script import Manager
import os

# COV = None
# if os.environ.get('FLASK_COVERAGE'):
#     import coverage
#     COV = coverage.coverage(branch=True, include='app/*')
#     COV.start()

manager = Manager(app=app)

if __name__ == '__main__':
    manager.run()

