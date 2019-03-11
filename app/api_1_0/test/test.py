from flask import request
from app.api_1_0 import api
from app import db

@api.route('/',method=['GET','POST'])
def test():
    return print('hello')