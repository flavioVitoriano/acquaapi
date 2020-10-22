from models import Client
from .base import BaseResource, BaseSingleResource


class ClientResource(BaseResource):
    class Meta:
        model = Client
        replace_fields = []
        field = "created_at"


class ClientSingleResource(BaseSingleResource):
    class Meta:
        model = Client
        fields = []
        replace_fields = []
