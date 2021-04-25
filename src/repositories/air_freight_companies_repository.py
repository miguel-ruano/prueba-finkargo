from src.models import AirFreightCompany

class AirFreightCompaniesRepository():
    """
    repositorio para las compañías de transporte de carga aérea
    """

    def save(self, company: AirFreightCompany) -> AirFreightCompany:
        if company != None:
            return company.save()
        return None