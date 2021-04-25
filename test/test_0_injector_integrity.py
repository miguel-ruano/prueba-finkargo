from .mock_injector import mock_injector
from src.db_mongo import MongoDb
from src.repositories import UsersRepository,AirFreightCompaniesRepository
from src.services import SecurityService, AirFreightCompanyAdminService

# checks each property provide by Injector has correct integrity

def test_injector_prop_env():
    """ env is instance """
    assert isinstance(mock_injector.env(), dict)
    assert isinstance(mock_injector.env.mongo(), dict)

def test_injector_prop_mongo_db():
    assert isinstance(mock_injector.mongo_db(), MongoDb)

def test_injector_users_repository():
    assert isinstance(mock_injector.users_repository(), UsersRepository)

def test_injector_air_freight_companies_repository():
    assert isinstance(mock_injector.air_freight_companies_repository(), AirFreightCompaniesRepository)

def test_injector_security_service():
    assert isinstance(mock_injector.security_service(), SecurityService)
    assert isinstance(mock_injector.security_service().users_repository, UsersRepository)

def test_injector_air_freight_companies_admin_service():
    assert isinstance(mock_injector.air_freight_companies_admin_service(), AirFreightCompanyAdminService)
    assert isinstance(mock_injector.air_freight_companies_admin_service().air_freight_companies_repository, AirFreightCompaniesRepository)