from flask import jsonify
import copy

def json_response(data):
    res = {
        "msg": "ok",
        "status": True,
        "state": 200,
        "data": data
    }
    return jsonify(res)

def params_error(data):
    res = {
        "msg": "参数错误",
        "status": False,
        "state": 403,
        "error": data
    }
    return jsonify(res)

def jsonChack(v,*args):
    val = copy.deepcopy(v)
    error = {}
    for i in args:
        val.pop(i)

    for i in val:
        if val[i] == "":
            error[i] = "该参数为空"
    return error