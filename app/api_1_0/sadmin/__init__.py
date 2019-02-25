from flask import Blueprint

sadmin = Blueprint('sadmin', __name__)

from .college import college
from .secretary import secretary
from .rank import book_rank