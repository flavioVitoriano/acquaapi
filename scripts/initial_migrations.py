from common import create_user
from flask_script import Command
from db import db
from migrations.create_user_client import create_tables


class CreateTables(Command):
    def run(self):
        create_tables()
