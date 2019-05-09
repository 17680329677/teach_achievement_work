from flask import Blueprint

normal = Blueprint('normal', __name__)

from .book import book
from . import reform_project,reform_paper,invigilate,innovation_project,option_info
