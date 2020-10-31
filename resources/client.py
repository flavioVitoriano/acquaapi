from models import Client
from .base import BaseResource, BaseSingleResource
from flask_restful import reqparse


page_parser = reqparse.RequestParser()
page_parser.add_argument("full_name_contains", type=str, default="")


class ClientResource(BaseResource):
    def filter(self, data):
        args = page_parser.parse_args()
        name = args.full_name_contains

        data = data.select().where(Client.full_name.contains(name))

        return data

    class Meta:
        model = Client
        replace_fields = []


class ClientSingleResource(BaseSingleResource):
    class Meta:
        model = Client
        fields = []
        replace_fields = []
