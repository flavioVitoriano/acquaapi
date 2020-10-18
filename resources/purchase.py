from models import Purchase, Move
from .base import BaseResource, BaseSingleResource


class PurchaseResource(BaseResource):
    def pos_post(self, obj):
        move = Move(
            value=obj.total,
            type=0,
            obs=f"GERADO DA ENTRADA {obj.id}",
            user=obj.user,
        )
        move.save()

    class Meta:
        model = Purchase
        replace_fields = []


class PurchaseSingleResource(BaseSingleResource):
    class Meta:
        model = Purchase
        fields = ["total"]
        replace_fields = []
