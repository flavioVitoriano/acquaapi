from flask import Flask
from flask_script import Manager
from flask_restful import Api
from resources import (
    ClientResource,
    UserResource,
    PurchaseResource,
    SaleResource,
    LoanResource,
    ClientSingleResource,
    PurchaseSingleResource,
    SaleSingleResource,
    LoanSingleResource,
    MoveResource,
    MoveSingleResource,
    PathResource,
    PathSingleResource,
    RoutesGroupStatusResource,
    MoveReportResource,
    RegisterShipMakeResource,
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
api.add_resource(SaleResource, "/sales/")
api.add_resource(SaleSingleResource, "/sales/<int:pk>/")
api.add_resource(LoanResource, "/loans/")
api.add_resource(LoanSingleResource, "/loans/<int:pk>/")
api.add_resource(MoveResource, "/moves/")
api.add_resource(MoveSingleResource, "/moves/<int:pk>/")
api.add_resource(PathResource, "/paths/")
api.add_resource(PathSingleResource, "/paths/<int:pk>/")
api.add_resource(RoutesGroupStatusResource, "/paths/status/")
api.add_resource(MoveReportResource, "/moves/report/")
api.add_resource(RegisterShipMakeResource, "/paths/<path_id>/register/")
