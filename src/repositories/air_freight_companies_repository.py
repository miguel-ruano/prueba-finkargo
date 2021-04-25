from src.models import AirFreightCompany


class AirFreightCompaniesRepository:
    """
    repositorio para las compañías de transporte de carga aérea
    """

    def save(self, company: AirFreightCompany) -> AirFreightCompany:
        if company != None:
            return company.save()
        raise ValueError("invalid_data")

    def get_by_id(self, id: str) -> AirFreightCompany:
        try:
            return AirFreightCompany.objects(id=id).first()
        except:
            return None

    def search(self, _filter: str) -> list:
        return list(
            AirFreightCompany.objects(name={"$regex": _filter, "$options": "i"})
        )

    def get_all(self) -> list:
        return list(AirFreightCompany.objects())

    def delete(self, company: AirFreightCompany) -> bool:
        if company != None:
            company.delete()
            return True
        raise ValueError("invalid_data")
