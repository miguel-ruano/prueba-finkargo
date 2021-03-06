from flask import Flask
from src.injector import Injector
from .admin import air_freight_companies_admin_controller
from .security import authentication_controller


def register(app: Flask, injector: Injector) -> Flask:
    """
    Registro de controladores para la aplicación
    """
    injector.wire(modules=[air_freight_companies_admin_controller, authentication_controller])
    app.register_blueprint(authentication_controller.authentication_controller())
    app.register_blueprint(
        air_freight_companies_admin_controller.air_freight_companies_adm_controller()
    )
    return app