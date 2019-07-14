from bson import ObjectId
from flask.json import JSONEncoder
from flask import jsonify as _jsonify

class CustomJSONEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return JSONEncoder.default(self, o)

# 处理返回的json格式
def jsonify(res, http_code=200, msg=''):
    res['code'] = http_code
    res['msg'] = msg
    return _jsonify(res), http_code