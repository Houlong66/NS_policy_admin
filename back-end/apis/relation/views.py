# coding=utf-8

from apis.base import jsonify
from apis.relation import relation_server
from apis.server import mongo

@relation_server.route("/relations", methods=["get"])
def test():
    data = [one for one in mongo.db.recommend_record.find()]
    res = dict()
    res["data"] = data
    return jsonify(res, http_code=200)