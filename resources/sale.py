from models import Sale
from .base import BaseResource, BaseSingleResource


class SaleResource(BaseResource):
    class Meta:
        model = Sale
        replace_fields = [{"field": "client", "attr": "client.id"}]


class SaleSingleResource(BaseSingleResource):
    class Meta:
        model = Sale
        fields = ["total"]
