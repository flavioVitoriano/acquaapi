from models import *
from db import db


def create_tables():
    with db:
        db.create_tables([User, Client, Purchase, Sale])


create_tables()
