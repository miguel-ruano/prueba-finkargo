from src.repositories import AirFreightCompaniesRepository
from src.providers import AirFreightCompanyRequest
from src.models import AirFreightCompany


class AirFreightCompanyAdminService:
    """
    Servicio de administración de las compañías de transporte de carga aérea
    """

    def __init__(self, air_freight_companies_repository: AirFreightCompaniesRepository):
        self.air_freight_companies_repository = air_freight_companies_repository

    def create(self, company_request: AirFreightCompanyRequest) -> AirFreightCompany:
        if company_request != None:
            if company_request.valid:
                air_freigth_company = company_request.to_company()
                return self.air_freight_companies_repository.save(
                    company=air_freigth_company
                )
            else:
                raise ValueError("invalid_data")
        else:
            raise Exception("error")

    def get_one(self, id: str) -> AirFreightCompany:
        if id != None:
            air_freigth_company = self.air_freight_companies_repository.get_by_id(id)
            if air_freigth_company == None:
                raise ValueError("not_found")
            return air_freigth_company
        else:
            raise Exception("error")

    def update(self, company_request: AirFreightCompanyRequest):
        if company_request != None:
            air_freigth_company = self.air_freight_companies_repository.get_by_id(
                company_request.id
            )
            if air_freigth_company == None:
                raise ValueError("not_found")

            if company_request.valid:
                air_freigth_company = company_request.to_company(
                    base=air_freigth_company
                )
                return self.air_freight_companies_repository.save(air_freigth_company)
            else:
                raise ValueError("invalid_data")
        else:
            raise Exception("error")

    def search(self, _filter: str):
        return (
            self.air_freight_companies_repository.search(_filter=_filter)
            if _filter != None and len(_filter) > 0
            else self.get_all()
        )

    def get_all(self):
        return self.air_freight_companies_repository.get_all()

    def delete(self, id: str) -> bool:
        if id == None or len(id) <= 0:
            raise Exception("error")

        air_freigth_company = self.air_freight_companies_repository.get_by_id(id=id)
        if air_freigth_company != None:
            delete = self.air_freight_companies_repository.delete(
                company=air_freigth_company
            )
            return delete
        else:
            raise ValueError("not_found")
