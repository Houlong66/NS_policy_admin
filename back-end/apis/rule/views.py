# coding=utf-8

from flask import jsonify
from apis.rule import rule_server
from apis.server import mongo

@rule_server.route("/rules", methods=["get"])
def test():
    expired = mongo.db.config.find_one({"recommend_expired_hours": {'$exists': True}})["recommend_expired_hours"]
    res = dict()
    res["expired"] = expired
    return jsonify(res)