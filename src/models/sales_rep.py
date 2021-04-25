from mongoengine import (
    EmbeddedDocument,
    StringField
)
class SalesRep(EmbeddedDocument):
    meta = {"strict": False}
    
    firstname = StringField()
    lastname = StringField()
    cell_phone = StringField()
    phone = StringField()
    email = StringField()