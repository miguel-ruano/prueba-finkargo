from flask import Blueprint, request, jsonify, abort, make_response
from flask_cors import CORS
from src.injector import Injector
from dependency_injector.wiring import Provide
from src.providers import AirFreightCompanyRequest
from src.services import AirFreightCompanyAdminService, SecurityService
from src.controllers.basic_response import BasicResponse


def air_freight_companies_adm_controller(
    service: AirFreightCompanyAdminService = Provide[
        Injector.air_freight_companies_admin_service
    ],
    security: SecurityService = Provide[Injector.security_service],
    settings: dict = Provide[Injector.env],
):

    # flask module
    controller = Blueprint("admin_freight_companies_controller", __name__)

    # cors
    CORS(controller, resources={r"/admin/*": {"origins": "*"}})

    def check_security() -> bool:
        try:
            return security.check_token(request.headers)
        except ValueError as error:
            BasicResponse.abort(401, error=Exception("Unauthorized"))
        except Exception as error:
            BaseException.abort(500, error=Exception("sys_error"))

    @controller.route("/admin/airfreightcompanies", methods=["POST"])
    def create():
        check_security()
        try:
            request_payload = request.get_json()
            company = AirFreightCompanyRequest(**request_payload)
            data = service.create(company_request=company)
            return BasicResponse(data.to_json_map()).to_json_response()
        except Exception as error:
            BasicResponse.abort(status=400, error=error)

    @controller.route("/admin/airfreightcompanies", methods=["PUT"])
    def update():
        check_security()
        try:
            request_payload = request.get_json()
            company = AirFreightCompanyRequest(**request_payload)
            data = service.update(company_request=company)
            return BasicResponse(data=data.to_json_map()).to_json_response()
        except Exception as error:
            BasicResponse.abort(status=400, error=error)

    @controller.route("/admin/airfreightcompanies", methods=["GET"])
    def search():
        check_security()
        try:
            _filter = request.args["filter"] if "filter" in request.args else None
            data = service.search(_filter=_filter)
            return BasicResponse(
                data=list(map(lambda item: item.to_json_map(), data))
            ).to_json_response()
        except Exception as error:
            BasicResponse.abort(status=400, error=error)

    @controller.route("/admin/airfreightcompanies/<id>", methods=["GET"])
    def get_one(id: str):
        check_security()
        try:
            data = service.get_one(id=id)
            return BasicResponse(data.to_json_map()).to_json_response()
        except Exception as error:
            BasicResponse.abort(status=400, error=error)

    @controller.route("/admin/airfreightcompanies/<id>", methods=["DELETE"])
    def delete(id: str):
        check_security()
        try:
            data = service.delete(id=id)
            return BasicResponse(data).to_json_response()
        except Exception as error:
            BasicResponse.abort(status=400, error=error)

    return controller