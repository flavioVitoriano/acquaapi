import peewee as pw
from db import BaseModel
from .user import User
from .client import Client
from datetime import datetime


class Move(BaseModel):
    type_choices = ((0, "Despesa"), (1, "Entrada"))
    user = pw.ForeignKeyField(User, backref="moves")
    value = pw.DecimalField(max_digits=10, decimal_places=2)
    obs = pw.TextField(null=True)
    type = pw.IntegerField(choices=type_choices, default=0)
    submit_date = pw.DateField(default=datetime.now)
