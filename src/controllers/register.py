from flask import Flask
from src.injector import Injector


def register(app: Flask, injector: Injector) -> Flask:
    """
    Registro de controladores para la aplicación
    """
    
    return app