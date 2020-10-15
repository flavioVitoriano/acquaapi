from models import Loan
from .base import BaseResource, BaseSingleResource


class LoanResource(BaseResource):
    class Meta:
        model = Loan
        replace_fields = [
            {"field": "client", "attr": "client.id"},
        ]


class LoanSingleResource(BaseSingleResource):
    class Meta:
        model = Loan
        fields = []
        replace_fields = [
            {"field": "client", "attr": "client.id"},
        ]
