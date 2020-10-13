from flask_restful import Resource
from flask import request
from models import Client
from decorators import token_required
from common.response import json_response
from playhouse.shortcuts import model_to_dict


class ClientResource(Resource):
    @token_required
    def get(self, user):
        data = Client.select().where(Client.user == user).dicts()
        return json_response(list(data), 200)

    @token_required
    def post(self, user):
        data = request.json

        if not data:
            return json_response({"message": "Cannot create client without data"}, 401)

        client = Client.create(**data, user=user)
        json_client = model_to_dict(client)
        json_client["user"] = user.public_id

        return json_response(json_client, 201)

    @token_required
    def patch(self, user, pk):
        data = request.json

        if not data:
            return json_response({"message": "Cannot update client without data"}, 401)

        fields = data.keys()
        client = Client.get(Client.id == pk & Client.user == user)

        for key in fields:
            setattr(client, key, data[key])

        client.save()
        json_client = model_to_dict(client)
        json_client["user"] = user.public_id

        return json_response(json_client, 200)

    @token_required
    def get_one(self, user, pk):
        client = Client.get(Client.user == user & Client.id == pk)
        json_client = model_to_dict(client)
        json_client["user"] = user.public_id

        return json_response(json_client, 200)
