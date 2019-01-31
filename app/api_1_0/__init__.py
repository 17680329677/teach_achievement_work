from flask import Blueprint

api = Blueprint('api', __name__)

from .login import login
from .college import college
from .secretary import secretary
