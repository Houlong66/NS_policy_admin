# coding=utf-8
from flask import Blueprint

rule_server = Blueprint("rule_server", __name__)

from . import views