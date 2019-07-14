# coding=utf-8

from flask import Flask
from flask_pymongo import PyMongo
from flask_cors import CORS
from apis.base import CustomJSONEncoder

from read_config import ConfigLoader

config = ConfigLoader()

app = Flask(__name__)
# 配置自定义的json解析,解决_id为ObjectID的问题
app.json_encoder = CustomJSONEncoder
# 配置跨域
CORS(app, supports_credentials=True)
# 连接MongoDB
app.config["MONGO_URI"]=f"mongodb://{config.get('mongoDB','host')}:{config.get('mongoDB','port')}/ai_system"
mongo = PyMongo(app)

from apis.relation import relation_server
from apis.rule import rule_server

app.register_blueprint(relation_server, url_prefix="/api/")
app.register_blueprint(rule_server, url_prefix="/api/")
