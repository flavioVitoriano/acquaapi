from models import Client
from .base import FilterDateResource, BaseSingleResource


class ClientResource(FilterDateResource):
    class Meta:
        model = Client
        replace_fields = []
        field = "created_at"


class ClientSingleResource(BaseSingleResource):
    class Meta:
        model = Client
        fields = []
        replace_fields = []
