# coding=utf-8

from apis.base import jsonify
from apis.relation import relation_server
from apis.server import mongo
from flask import request
from bson import ObjectId

@relation_server.route("/relations", methods=["get"])
def index():
    data = [one for one in mongo.db.relations.find()]
    res = dict()
    res["data"] = data
    return jsonify(res, http_code=200)

@relation_server.route("/relations", methods=["post"])
def store():
    data = dict()
    data["word"] = (request.form.get("word")).split(',')
    data["type"] = request.form.get("type", "")
    data["priority"] = int(request.form.get("priority"))
    data["relation"] = request.form.get("relation", "")
    mongo.db.relations.insert_one(data)
    res = dict()
    return jsonify(res)

@relation_server.route("/relations", methods=["put"])
def update():
    mongo.db.relations.update_one(
        {"_id": ObjectId(request.form.get("relation_id"))},
        {
            "$set": {
                "word": (request.form.get("word")).split(','),
                "type": request.form.get("type", ""),
                "priority": int(request.form.get("priority")),
                "relation": request.form.get("relation", "")
            }
        }
    )
    res = dict()
    return jsonify(res)

@relation_server.route("/relations/<id>", methods=["delete"])
def delete(id):
    mongo.db.relations.delete_many({"_id":ObjectId(id)})
    res = dict()
    return jsonify(res)
