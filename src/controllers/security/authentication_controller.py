from flask import Blueprint, request, jsonify, abort, make_response
from flask_cors import CORS
from src.injector import Injector
from dependency_injector.wiring import Provide
from src.services import SecurityService
from src.controllers.basic_response import BasicResponse


def authentication_controller(
    service: SecurityService = Provide[Injector.security_service],
    settings: dict = Provide[Injector.env],
):

    # flask module
    controller = Blueprint("authentication_controller", __name__)

    # cors
    CORS(controller, resources={r"/security/auth/*": {"origins": "*"}})

    @controller.route("/security/auth/token", methods=["POST"])
    def authentication():
        authorization = request.authorization
        if (
            not authorization
            or not authorization.username
            or not authorization.password
        ):
            BasicResponse.abort(
                401, Exception('Basic realm: "login required"')
            )
        try:
            authentication = service.authenticate(
                user_login=authorization.username, user_password=authorization.password
            )
            return jsonify(authentication)
        except ValueError as error:
            BasicResponse.abort(401, error=error)
        except Exception as error:
            BasicResponse.abort(500, error=Exception("sys error"))

    return controller