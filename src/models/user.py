from .entity_base import EntityBase
from mongoengine import StringField


class User(EntityBase):

    login = StringField(required=True, primary_key=True)
    password = StringField(required=True)
    salt = StringField(required=True)
