# mock injector
import unittest.mock
from src.injector import Injector
from .mongo_mock import MockMongoDb
from .constants import user

mock_injector = Injector()
mock_injector.env.from_yaml("environment/environment.yml")
mock_injector.mongo_db.override(MockMongoDb())
# set credentials for tests
mock_injector.env()["security"]["seeds"] = {"user": user}
# manual connection to mongomock
mock_injector.mongo_db().connect()
mock_injector.security_service().init_seeds()
