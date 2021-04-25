from src.models import AirFreightCompany, SalesRep


def has_missing_keys(obj, keys):
    missing = list(
        filter(
            (lambda key: not hasattr(obj, key)),
            keys,
        )
    )
    return len(missing) <= 0


class SalesRepRequest:
    firstname: str
    lastname: str
    cell_phone: str
    phone: str
    email: str

    def __init__(self, *args, **kwargs):
        if kwargs != None:
            self.__dict__.update(kwargs)

    @property
    def valid(self) -> bool:
        return (
            has_missing_keys(self, ["firstname", "cell_phone", "email"])
            and self.firstname != None
            and self.cell_phone != None
            and self.email != None
        )

    def to_salesrep(self):
        if self.valid:
            rep = SalesRep()
            rep.firstname = self.firstname
            rep.lastname = self.lastname if hasattr(self, "lastname") else None
            rep.cell_phone = self.cell_phone
            rep.phone = self.phone if hasattr(self, "phone") else None
            rep.email = self.email
            return rep
        return None


class AirFreightCompanyRequest:
    id: str
    name: str
    address: str
    countries_wh_presence: list
    sales_rep: dict

    def __init__(self, *args, **kwargs):
        if kwargs != None:
            self.__dict__.update(kwargs)

    @property
    def valid(self) -> bool:
        return has_missing_keys(
            self, ["name", "address", "countries_wh_presence", "sales_rep"]
        ) and (
            self.name != None
            and self.address != None
            and self.countries_wh_presence != None
            and self.sales_rep != None
        )

    def to_company(self, base: AirFreightCompany = None) -> AirFreightCompany:
        if self.valid:
            company = base if base != None else AirFreightCompany()
            if hasattr(self, "id"):
                setattr(company, "id", self.id)
            company.name = self.name
            company.address = self.address
            company.countries_wh_presence = self.countries_wh_presence
            company.sales_rep = SalesRepRequest(**self.sales_rep).to_salesrep()
            return company
        return None