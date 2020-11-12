import peewee as pw
from db import BaseModel
from datetime import datetime
from .base import TimezoneField


class User(BaseModel):
    public_id = pw.CharField(max_length=255,unique=True)
    full_name = pw.CharField(max_length=255, null=True)
    username = pw.CharField(max_length=20, unique=True)
    password = pw.CharField(max_length=255)
    address = pw.CharField(max_length=255, null=True)
    number_address = pw.CharField(max_length=6, null=True)
    city = pw.CharField(max_length=255, null=True)
    state = pw.CharField(max_length=2, null=True)
    phone = pw.CharField(max_length=255, null=True)
    payment_day = pw.IntegerField(default=1)
    created_at = TimezoneField(default=datetime.now)
