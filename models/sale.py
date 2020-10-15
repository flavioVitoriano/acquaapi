import peewee as pw
from db import BaseModel
from .user import User
from .client import Client
from datetime import datetime


class Sale(BaseModel):
    user = pw.ForeignKeyField(User, backref="sales")
    client = pw.ForeignKeyField(Client, backref="sales")
    quantity = pw.IntegerField(default=1)
    value = pw.DecimalField(max_digits=10, decimal_places=2)
    discounts = pw.DecimalField(max_digits=10, decimal_places=2, default=0)
    submit_date = pw.DateTimeField(default=datetime.now)

    @property
    def total(self):
        return (self.quantity * float(self.value)) - float(self.discounts)
