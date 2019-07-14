# coding=utf-8
from flask import Blueprint

relation_server = Blueprint("relation_server", __name__)

from . import views
