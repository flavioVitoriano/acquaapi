from models import Client
from .base import BaseResource, BaseSingleResource


class ClientResource(BaseResource):
    class Meta:
        model = Client
        replace_fields = []


class ClientSingleResource(BaseSingleResource):
    class Meta:
        model = Client
        fields = []
