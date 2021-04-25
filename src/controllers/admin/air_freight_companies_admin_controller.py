from flask import Blueprint, request, jsonify, abort, make_response
from flask_cors import CORS
from src.injector import Injector
from dependency_injector.wiring import Provide
from src.providers import AirFreightCompanyRequest
from src.services import AirFreightCompanyAdminService
from src.controllers.basic_response import BasicResponse


def air_freight_companies_adm_controller(
    service: AirFreightCompanyAdminService = Provide[
        Injector.air_freight_companies_admin_service
    ],
    settings: dict = Provide[Injector.env],
):

    # flask module
    controller = Blueprint("authentication_controller", __name__)

    # cors
    CORS(controller, resources={r"/admin/*": {"origins": "*"}})

    @controller.route("/admin/airfreightcompanies", methods=["POST"])
    def create():
        try:
            request_payload = request.get_json()
            company = AirFreightCompanyRequest(**request_payload)
            data = service.create(company_request=company)
            return BasicResponse(data.to_json_map()).to_json_response()
        except Exception as error:
            BasicResponse.abort(status=400, error=error)

    @controller.route("/admin/airfreightcompanies", methods=["PUT"])
    def update():
        try:
            request_payload = request.get_json()
            company = AirFreightCompanyRequest(**request_payload)
            data = service.update(company_request=company)
            return BasicResponse(data=data.to_json_map()).to_json_response()
        except Exception as error:
            BasicResponse.abort(status=400, error=error)

    @controller.route("/admin/airfreightcompanies", methods=["GET"])
    def search():
        try:
            _filter = (
                request.args["filter"]
                if "filter" in request.args
                else abort(
                    400, BasicResponse(status=400, error="filter parameter is required")
                )
            )
            data = service.search(_filter=_filter)
            return BasicResponse(
                data=list(map(lambda item: item.to_json_map(), data))
            ).to_json_response()
        except Exception as error:
            BasicResponse.abort(status=400, error=error)

    @controller.route("/admin/airfreightcompanies/<id>", methods=["GET"])
    def get_one(id: str):
        try:
            data = service.get_one(id=id)
            return BasicResponse(data.to_json_map()).to_json_response()
        except Exception as error:
            BasicResponse.abort(status=400, error=error)

    @controller.route("/admin/airfreightcompanies/<id>", methods=["DELETE"])
    def delete(id: str):
        try:
            data = service.delete(id=id)
            return BasicResponse(data).to_json_response()
        except Exception as error:
            BasicResponse.abort(status=400, error=error)

    return controller