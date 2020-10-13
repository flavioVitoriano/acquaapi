from common import create_user
from flask_script import Command
from db import db


class CreateUser(Command):

    def run(self):
        db.connect()

        camps = {
            "username": "Usuário: ",
            "password": "Senha: ",
        }

        data = dict()

        for camp in camps.keys():
            data[camp] = input(camps[camp])

        create_user(**data)
        print("Usuário criado com sucesso!")
