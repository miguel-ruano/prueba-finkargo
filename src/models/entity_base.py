from mongoengine import Document, DateTimeField
import datetime
import json


class EntityBase(Document):
    """
    modelo base de persistencia de los modelos
    """

    dateTimeFormat = "%Y-%m-%dT%H:%M:%SZ"
    meta = {"abstract": True, "strict": False}

    created_at = DateTimeField(default=datetime.datetime.utcnow)
    updated_at = DateTimeField(default=datetime.datetime.utcnow)

    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = datetime.datetime.utcnow()
        self.updated_at = datetime.datetime.utcnow()
        return super(EntityBase, self).save(*args, **kwargs)

    def to_json_map(self):
        base_json = json.loads(self.to_json(use_db_field=False))
        base_json["created_at"] = self.created_at.strftime(EntityBase.dateTimeFormat)
        base_json["updated_at"] = self.updated_at.strftime(EntityBase.dateTimeFormat)

        if "id" in base_json:
            base_json["id"] = str(self.id)

        if "_id" in base_json:
            base_json.pop("_id")
        return base_json
