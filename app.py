from flask import Flask
from flask_script import Manager
from flask_restful import Api
from resources import ClientResource, UserResource
from db import db as database

app = Flask(__name__)
api = Api(app)
manager = Manager(app)


@app.before_request
def before_request():
    database.connect()


@app.after_request
def after_request(response):
    database.close()
    return response


# api
api.add_resource(UserResource, "/auth/")
api.add_resource(ClientResource, "/clients/", "/clients/<int:pk>/")
