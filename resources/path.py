from flask_restful import Resource
from models import Path
from .base import BaseResource, BaseSingleResource
from datetime import timedelta, date
from common.response import json_response
from decorators import token_required


class PathResource(BaseResource):
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
