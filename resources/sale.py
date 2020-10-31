from models import Sale, Move
from .base import FilterDateResource, BaseSingleResource
from models import Client
from flask_restful import reqparse


filter_parser = reqparse.RequestParser()
filter_parser.add_argument("client", type=int)


class SaleResource(FilterDateResource):
    def pos_post(self, obj):
        move = Move(
            value=obj.total,
            type=1,
            obs=f"GERADO DA VENDA {obj.id}",
            user=obj.user,
        )
        move.save()

    def parse_item(self, item):
        item["client"] = Client.select().where(Client.id == item["client"]).get()

        item["client"] = {
            "id": item["client"].id,
            "full_name": item["client"].full_name,
        }

        return item

    def filter(self, data):
        data = super().filter(data)
        args = filter_parser.parse_args()
        client = args.client

        if not client:
            return data

        client_obj = Client.get_by_id(client)

        data = data.select().where(Sale.client == client_obj)

        return data

    class Meta:
        model = Sale
        replace_fields = [
            {"field": "client", "attr": "client.id"},
        ]
        field = "submit_date"


class SaleSingleResource(BaseSingleResource):
    class Meta:
        model = Sale
        fields = ["total"]
        replace_fields = [
            {"field": "client", "attr": "client.id"},
        ]
