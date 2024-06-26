from database.models.components.base_models import BaseModel
from database.models.user import User
from peewee import CharField, ForeignKeyField


class App(BaseModel):
    user = ForeignKeyField(User, backref="apps")
    app_type = CharField(null=True)
    name = CharField(null=True)
    status = CharField(null=True)
