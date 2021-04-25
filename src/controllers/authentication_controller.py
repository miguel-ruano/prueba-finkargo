from flask import Blueprint, request, jsonify, abort
from flask_cors import CORS
from src.injector import Injector
from dependency_injector.wiring import Provide


def authentication_controller(
    service: SecurityService = Provide[Injector.security_service],
    settings: dict = Provide[Injector.env],
):

    # flask module
    controller = Blueprint("authentication_controller", __name__)

    # cors
    CORS(controller, resources={r"/api/*": {"origins": "*"}})

    @controller.route("security/auth/token", methods=["POST"])
    def authentication():
        request_payload = request.get_json()
        return jsonify(request_payload)