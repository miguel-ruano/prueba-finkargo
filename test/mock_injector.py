# mock injector
import unittest.mock
from src.injector import Injector
from .mongo_mock import MockMongoDb


mock_injector = Injector()
mock_injector.env.from_yaml("environment/environment.yml")
mock_injector.mongo_db.override(MockMongoDb())
# manual connection to mongomock
mock_injector.mongo_db().connect()