from flask import Blueprint

student = Blueprint('student', __name__)

from . import password,distribution_result,distribution_reform