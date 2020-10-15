import peewee as pw
from db import BaseModel
from .user import User
from .client import Client
from datetime import datetime


class Loan(BaseModel):
    status_choices = ((0, "Pending"), (1, "Accepted"), (2, "Rejected"))
    user = pw.ForeignKeyField(User, backref="loans")
    client = pw.ForeignKeyField(Client, backref="loans")
    quantity = pw.IntegerField(default=1)
    order_date = pw.DateTimeField(default=datetime.now)
    accept_date = pw.DateTimeField(null=True)
    status = pw.IntegerField(default=0, choices=status_choices)
