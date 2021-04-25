from .entity_base import EntityBase
from mongoengine import StringField, EmbeddedDocumentField, ListField
from .sales_rep import SalesRep


class AirFreightCompany(EntityBase):
    name = StringField(required=True)
    address = StringField(required=True)
    countries_wh_presence = ListField(StringField())
    sales_rep = EmbeddedDocumentField(SalesRep)