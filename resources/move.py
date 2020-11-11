from models import Move
from .base import FilterDateResource, BaseSingleResource
from flask_restful import reqparse
from datetime import date, timedelta
from flask_restful import Resource
from common.response import json_response
from decorators import token_required
from peewee import fn

default_end_date = (date.today() + timedelta(days=30)).isoformat()

parser = reqparse.RequestParser()
parser.add_argument("initial_date", type=str, default=date.today().isoformat())
parser.add_argument("end_date", type=str, default=default_end_date)


class MoveResource(FilterDateResource):
    class Meta:
        model = Move
        replace_fields = [{"field": "user", "attr": "user.public_id"}]
        field = "submit_date"


class MoveSingleResource(BaseSingleResource):
    class Meta:
        model = Move
        fields = []
        replace_fields = []


class MoveReportResource(Resource):
    @token_required
    def get(self, user):
        args = parser.parse_args()
        initial_date = date.fromisoformat(args.initial_date)
        end_date = date.fromisoformat(args.end_date)

        data = Move.select().where(
            Move.submit_date.between(initial_date, end_date) & Move.user == user
        )

        out = data.select(fn.SUM(Move.value).alias("total")).where(
            Move.type == 1
        )
        entry = data.select(fn.SUM(Move.value).alias("total")).where(
            Move.type == 0
        )

        out = out[0].total
        if out is None:
            out = 0
        entry = entry[0].total
        if entry is None:
            entry = 0

        return json_response(
            {"entry_sum": entry, "out_sum": out, "profit": (entry - out)}, 200
        )
