from models import Sale, Move
from .base import BaseResource, BaseSingleResource


class SaleResource(BaseResource):
    def pos_post(self, obj):
        move = Move(
            value=obj.total,
            type=1,
            obs=f"GERADO DA VENDA {obj.id}",
            user=obj.user,
        )
        move.save()

    class Meta:
        model = Sale
        replace_fields = [
            {"field": "client", "attr": "client.id"},
        ]


class SaleSingleResource(BaseSingleResource):
    class Meta:
        model = Sale
        fields = ["total"]
        replace_fields = [
            {"field": "client", "attr": "client.id"},
        ]
