from src.repositories import AirFreightCompaniesRepository


class AirFreightCompanyAdminService:
    """
    Servicio de administración de las compañías de transporte de carga aérea
    """

    def __init__(self, air_freight_companies_repository: AirFreightCompaniesRepository):
        self.air_freight_companies_repository = air_freight_companies_repository

    def save(self):
        return None

    def search(self):
        return None

    def update(self):
        return None

    def delete(self):
        return None