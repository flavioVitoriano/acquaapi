from flask import Flask
from flask_script import Manager
from flask_restful import Api
from resources import (
    ClientResource,
    UserResource,
    PurchaseResource,
    ClientSingleResource,
    PurchaseSingleResource,
)
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
api.add_resource(ClientResource, "/clients/")
api.add_resource(ClientSingleResource, "/clients/<int:pk>/")
api.add_resource(PurchaseResource, "/purchases/")
api.add_resource(PurchaseSingleResource, "/purchases/<int:pk>/")
