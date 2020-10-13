from flask import make_response, jsonify


def json_response(data, code):
    return make_response(jsonify(data), code)
