from flask import Blueprint

normal = Blueprint('normal', __name__)

from .book import book
