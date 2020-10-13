import peewee as pw
from db import BaseModel
from .user import User


class Client(BaseModel):
    user = pw.ForeignKeyField(User, backref="clients")
    full_name = pw.CharField(max_length=255)
    address = pw.CharField(max_length=255, null=True)
    number_address = pw.CharField(max_length=6, null=True)
    city = pw.CharField(max_length=255, null=True)
    phone = pw.CharField(max_length=255, null=True)
    preferred_price = pw.DecimalField(max_digits=10, decimal_places=2, default=0)
