from models import Sale, Move
from .base import BaseResource, BaseSingleResource
from models import Client
from flask_restful import reqparse
from datetime import date, timedelta

default_end_date = (date.today() + timedelta(days=30)).isoformat()

filter_parser = reqparse.RequestParser()
filter_parser.add_argument("client", type=int)
filter_parser.add_argument(
    "start_date", type=str, default=date.today().isoformat()
)
filter_parser.add_argument("end_date", type=str, default=default_end_date)


class SaleResource(BaseResource):
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
        args = filter_parser.parse_args()
        client = args.client

        if client:
            client_obj = Client.get_by_id(client)
            data = data.select().where(Sale.client == client_obj)

        try:
            start_date = date.fromisoformat(args.start_date)
            end_date = date.fromisoformat(args.end_date)
        except ValueError:
            return data

        data = data.select().where(Sale.submit_date.between(start_date, end_date))

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
