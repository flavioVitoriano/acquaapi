from flask import request, jsonify
from functools import wraps
from models import User
import os
import jwt
from common import json_response


def token_required(f):
    @wraps(f)
    def decorator(self, *args, **kwargs):

        token = None

        if "Authorization" in request.headers:
            authorization = request.headers.get("Authorization")
            token = authorization.split(" ")[-1]

        if not token:
            return json_response({"message": "a valid token is missing"}, 401)

        try:
            data = jwt.decode(token, os.environ.get("SECRET_KEY"))
            current_user = User.get(public_id=data["public_id"])

        except jwt.exceptions.DecodeError:
            return json_response({"message": "token is invalid"}, 401)

        return f(self, current_user, *args, **kwargs)

    return decorator
