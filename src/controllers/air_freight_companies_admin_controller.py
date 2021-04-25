from flask import Blueprint, request, jsonify, abort
from flask_cors import CORS
from src.injector import Injector
from dependency_injector.wiring import Provide


def air_freight_companies_adm_controller(
    service: AirFreightCompaniesAdminService = Provide[
        Injector.air_freight_companies_admin_service
    ],
    settings: dict = Provide[Injector.env],
):

    # flask module
    controller = Blueprint("authentication_controller", __name__)

    # cors
    CORS(controller, resources={r"/api/*": {"origins": "*"}})

    @controller.route("admin/airfreightcompanies", methods=["POST"])
    def create():
        return jsonify("ok")

    @controller.route("admin/airfreightcompanies", methods=["PUT"])
    def update():
        return jsonify("ok")

    @controller.route("admin/airfreightcompanies", methods=["GET"])
    def search():
        return jsonify("ok")

    @controller.route("admin/airfreightcompanies/<id>", methods=["GET"])
    def get_one(id: str):
        return jsonify("ok")

    @controller.route("admin/airfreightcompanies/<id>", methods=["DELETE"])
    def delete(id: str):
        return jsonify("ok")