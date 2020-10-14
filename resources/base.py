from flask_restful import Resource
from flask import request
from decorators import token_required
from common.response import json_response
from playhouse.shortcuts import model_to_dict


class BaseResource(Resource):
    @token_required
    def get(self, user):
        data = self.Meta.model.select().where(self.Meta.model.user == user).dicts()
        return json_response(list(data), 200)

    @token_required
    def post(self, user):
        data = request.json

        if not data:
            return json_response({"message": "Cannot create obj without data"}, 401)

        obj = self.Meta.model.create(**data, user=user)
        json_obj = model_to_dict(obj)
        json_obj["user"] = user.public_id

        return json_response(json_obj, 201)


class BaseSingleResource(Resource):
    @token_required
    def patch(self, user, pk):
        data = request.json
        data.pop("user", "")

        if not data:
            return json_response({"message": "Cannot update obj without data"}, 401)

        fields = data.keys()
        obj = self.Meta.model.get(
            self.Meta.model.id == pk & self.Meta.model.user == user
        )
        for key in fields:
            setattr(obj, key, data[key])

        obj.save()
        json_obj = model_to_dict(obj)
        json_obj["user"] = user.public_id

        return json_response(json_obj, 200)

    @token_required
    def get(self, user, pk):
        obj = self.Meta.model.get(
            self.Meta.model.user == user & self.Meta.model.id == pk
        )
        json_obj = model_to_dict(obj)
        json_obj["user"] = user.public_id

        if self.Meta.fields:
            for field in self.Meta.fields:
                json_obj[field] = getattr(obj, field)

        return json_response(json_obj, 200)

    def delete(self, user, pk):
        obj = self.Meta.model.get(
            self.Meta.model.user == user & self.Meta.model.id == pk
        )

        obj.delete_instance()

        json_obj = model_to_dict(obj)
        json_obj["user"] = user.public_id

        if self.Meta.fields:
            for field in self.Meta.fields:
                json_obj[field] = getattr(obj, field)

        return json_response(json_obj, 200)
