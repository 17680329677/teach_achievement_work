from flask import Flask, Blueprint, views
from app.handler.auth import *
from app.handler.book import *
from app.handler.certificate_info import *
from app.handler.college import *
from app.handler.innovation_project import *
from app.handler.invigilate_info import *
from app.handler.reform_paper import *
from app.handler.reform_project import *
from app.handler.student import *
from app.handler.teacher import *