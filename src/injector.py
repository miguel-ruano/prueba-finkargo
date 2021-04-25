from dependency_injector import providers, containers
from .db_mongo import MongoDb
from src.repositories import AirFreightCompaniesRepository, UsersRepository
from src.services import SecurityService, AirFreightCompanyAdminService


class Injector(containers.DeclarativeContainer):
    """
    Inyector de dependencias de la aplicación
    """

    env = providers.Configuration()
    # components
    mongo_db = providers.Singleton(
        MongoDb,
        host=env.mongo.host,
        database=env.mongo.database,
        port=env.mongo.port,
        auth=env.mongo.auth,
    )

    users_repository = providers.Singleton(UsersRepository)
    air_freight_companies_repository = providers.Singleton(AirFreightCompaniesRepository)

    security_service = providers.Singleton(
        SecurityService, users_repository=users_repository, security = env.security
    )

    air_freight_companies_admin_service = providers.Singleton(
        AirFreightCompanyAdminService,
        air_freight_companies_repository=air_freight_companies_repository,
    )
