from flask import request
from flask_restful import Resource
from models import User
from common import check_passwords, json_response
import jwt
import datetime
import os


class UserResource(Resource):
    def post(self):
        auth = request.json

        if not auth or not auth.get("username", None) or not auth.get("password", None):
            return json_response({"message": "could not verify"}, 400)

        user = User.get(username=auth["username"])

        if check_passwords(auth["password"], user.password):
            token = jwt.encode(
                {
                    "public_id": user.public_id,
                    "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=24),
                },
                os.environ.get("SECRET_KEY"),
            )
            return json_response({"token": token.decode("UTF-8")}, 201)

        return json_response({"message": "could not verify"}, 400)
