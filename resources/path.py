from flask_restful import Resource
from models import Path, Client, Move
from .base import BaseResource, BaseSingleResource
from datetime import timedelta, date
from common.response import json_response
from decorators import token_required
from flask_restful import reqparse


default_end_date = (date.today() + timedelta(days=30)).isoformat()

filter_parser = reqparse.RequestParser()
filter_parser.add_argument("client", type=int)
filter_parser.add_argument(
    "start_date", type=str, default=date.today().isoformat()
)
filter_parser.add_argument("end_date", type=str, default=default_end_date)


class PathResource(BaseResource):
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
            data = data.select().where(Path.client == client_obj)

        try:
            start_date = date.fromisoformat(args.start_date)
            end_date = date.fromisoformat(args.end_date)
        except ValueError:
            return data

        data = data.select().where(
            Path.last_ship_date.between(start_date, end_date)
        )

        return data

    class Meta:
        model = Path
        replace_fields = [{"field": "client", "attr": "client.id"}]


class PathSingleResource(BaseSingleResource):
    class Meta:
        model = Path
        fields = ["total"]
        replace_fields = [{"field": "client", "attr": "client.id"}]


class RoutesGroupStatusResource(Resource):
    @token_required
    def get(self, user):
        routes = Path.select().where(Path.user == user)

        def parse(item):
            next_ship_date = item.last_ship_date + timedelta(days=item.step_days)
            now_date = date.today()
            result = next_ship_date - now_date
            days = result.days
            status = "atrasado"

            if days <= 0:
                status = "atrasado"
            if days > item.warning_sub_day:
                status = "no prazo"
            else:
                status = "atenção"

            return {
                "path_id": item.id,
                "client_id": item.client.id,
                "until_days": days,
                "status": status,
            }

        result = map(parse, routes)

        return json_response(list(result), 200)


class RegisterShipMakeResource(Resource):
    @token_required
    def put(self, user, path_id):
        path_obj = (
            Path.select().where(Path.user == user, Path.id == path_id).get()
        )

        path_obj.last_ship_date = date.today()

        move = Move(
            value=path_obj.total,
            type=0,
            obs=f"GERADO DA VENDA DA ROTA {path_obj.id}",
            user=user,
        )

        path_obj.save()
        move.save()

        result = {"msg": "sucesso"}

        return json_response(result, 200)
