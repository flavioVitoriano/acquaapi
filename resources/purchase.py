from models import Purchase, Move
from .base import BaseResource, BaseSingleResource, FilterDateResource


class PurchaseResource(FilterDateResource):
    def pos_post(self, obj):
        move = Move(
            value=obj.total,
            type=1,
            obs=f"GERADO DA COMPRA {obj.id}",
            user=obj.user,
        )
        move.save()

    class Meta:
        model = Purchase
        replace_fields = []
        field = "submit_date"


class PurchaseSingleResource(BaseSingleResource):
    class Meta:
        model = Purchase
        fields = ["total"]
        replace_fields = []
