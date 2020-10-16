from flask_restful import Resource
from flask import request
from decorators import token_required
from common.response import json_response
from playhouse.shortcuts import model_to_dict
from functools import reduce
from flask_restful import reqparse

page_parser = reqparse.RequestParser()
page_parser.add_argument("page", type=int, default=1)
page_parser.add_argument("limit", type=int, default=5)


def deepgetattr(obj, attr):
    """Recurses through an attribute chain to get the ultimate value."""
    return reduce(getattr, attr.split("."), obj)


class BaseResource(Resource):
    def paginate(self, data):
        args = page_parser.parse_args()
        return data.paginate(args.page, args.limit)

    @token_required
    def get(self, user):
        data = self.Meta.model.select().where(self.Meta.model.user == user).dicts()
        data = self.paginate(data)

        def parse(item):
            item["user"] = user.public_id
            return item

        data = map(parse, data)

        return json_response(list(data), 200)

    @token_required
    def post(self, user):
        data = request.json

        if not data:
            return json_response({"message": "Cannot create obj without data"}, 401)

        obj = self.Meta.model.create(**data, user=user)
        json_obj = model_to_dict(obj)
        json_obj["user"] = user.public_id

        if self.Meta.replace_fields:
            for field in self.Meta.replace_fields:
                json_obj[field["field"]] = deepgetattr(obj, field["attr"])

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

        if self.Meta.fields:
            for field in self.Meta.fields:
                json_obj[field] = getattr(obj, field)

        if self.Meta.replace_fields:
            for field in self.Meta.replace_fields:
                json_obj[field["field"]] = deepgetattr(obj, field["attr"])

        return json_response(json_obj, 200)

    @token_required
    def get(self, user, pk):
        obj = self.Meta.model.get(self.Meta.model.id == pk)

        if obj.user.id is not user.id:
            return json_response({"erro": "cliente nao encontrado"}, 404)

        json_obj = model_to_dict(obj)
        json_obj["user"] = user.public_id

        if self.Meta.fields:
            for field in self.Meta.fields:
                json_obj[field] = getattr(obj, field)

        if self.Meta.replace_fields:
            for field in self.Meta.replace_fields:
                json_obj[field["field"]] = deepgetattr(obj, field["attr"])

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

        if self.Meta.replace_fields:
            for field in self.Meta.replace_fields:
                json_obj[field["field"]] = deepgetattr(obj, field["attr"])

        return json_response(json_obj, 200)
