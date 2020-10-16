from models import *
from db import db


def create_tables():
    with db:
        db.create_tables([User, Client, Purchase, Sale, Loan, Move, Path])


create_tables()
