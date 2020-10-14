import peewee as pw
from db import BaseModel
from .user import User
from datetime import datetime


class Purchase(BaseModel):
    user = pw.ForeignKeyField(User, backref="purchases")
    quantity = pw.IntegerField(default=1)
    value = pw.DecimalField(max_digits=10, decimal_places=2)
    submit_data = pw.DateTimeField(default=datetime.now)

    @property
    def total(self):
        return self.quantity * float(self.value)
