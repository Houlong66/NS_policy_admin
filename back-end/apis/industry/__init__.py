# coding=utf-8
from flask import Blueprint

industry_server = Blueprint("industry_server", __name__)

from . import views
