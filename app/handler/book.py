import os
import easyapi
from flask import Flask, Blueprint, jsonify, send_file, request, current_app
from easyapi_tools.errors import BusinessError
from flask_jwt import jwt_required, current_identity
import app.core as controller
import app.service as service
from app.config import Config


class BookHandler(easyapi.FlaskBaseHandler):
    __controller__ = controller.BookController
book_bp = Blueprint(name='books', import_name='books', url_prefix='')
easyapi.register_api(app=book_bp, view=BookHandler, endpoint='book_api', url='/books')


class BookRankHandler(easyapi.FlaskBaseHandler):
    __controller__ = controller.BookRankController
book_rank_bp = Blueprint(name='book_ranks', import_name='book_ranks', url_prefix='')
easyapi.register_api(app=book_rank_bp, view=BookRankHandler, endpoint='book_rank_api', url='/book_ranks')

