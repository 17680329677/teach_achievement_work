from flask import Blueprint

sadmin = Blueprint('sadmin', __name__)

from .college import college
from .secretary import secretary
from .rank import book_rank,certificate_rank,project_type,project_child_type,teacher_title,teacher_type,project_rank,innovation_rank,teacher_category
from . import password,semester_info