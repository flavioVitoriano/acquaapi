from models import Move
from .base import BaseResource, BaseSingleResource


class MoveResource(BaseResource):
    class Meta:
        model = Move
        replace_fields = [{"field": "user", "attr": "user.public_id"}]


class MoveSingleResource(BaseSingleResource):
    class Meta:
        model = Move
        fields = []
        replace_fields = []
