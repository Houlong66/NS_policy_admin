# coding=utf-8

import json
from apis.base import jsonify
from apis.industry import industry_server
from apis.server import mongo
from flask import request
from bson import ObjectId

@industry_server.route("/industries", methods=["get"])
def index():
    data = [one for one in mongo.db.industry_standard.find()]
    res = dict()
    res["data"] = data
    return jsonify(res, http_code=200)

@industry_server.route("/industries", methods=["post"])
def update():
    data = request.form.get('data')
    data = json.loads(data)
    data['_id'] = ObjectId(data['_id'])
    mongo.db.industry_standard.update_one({"_id":data.get('_id')}, {'$set':data})
    res = dict()
    return jsonify(res)

# @relation_server.route("/relations/<id>", methods=["delete"])
# def delete(id):
#     mongo.db.relations.delete_many({"_id":ObjectId(id)})
#     res = dict()
#     return jsonify(res)
