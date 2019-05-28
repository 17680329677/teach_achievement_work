from flask import Blueprint

cadmin = Blueprint('cadmin', __name__)

from . import department,teacher_info,title_granted,option_info,book,\
    reform_project,reform_paper,innovation_project,invigilate,invigilate_statistics,class_info,\
    distribution_info,distribution_desire,students_import,distribution_result
