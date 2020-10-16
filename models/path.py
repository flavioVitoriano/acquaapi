import peewee as pw
from db import BaseModel
from .user import User
from .client import Client
from datetime import datetime


class Path(BaseModel):
    user = pw.ForeignKeyField(User, backref="paths")
    client = pw.ForeignKeyField(Client, backref="paths")
    step_days = pw.IntegerField(default=30)
    last_ship_date = pw.DateField(default=datetime.now)
    quantity = pw.IntegerField(default=1)
    value = pw.DecimalField(decimal_places=2, max_digits=10)
    warning_sub_day = pw.IntegerField(default=1)

    @property
    def total(self):
        return self.quantity * float(self.value)
