from models import Purchase
from .base import BaseResource, BaseSingleResource


class PurchaseResource(BaseResource):
    class Meta:
        model = Purchase
        replace_fields = []


class PurchaseSingleResource(BaseSingleResource):
    class Meta:
        model = Purchase
        fields = ["total"]
