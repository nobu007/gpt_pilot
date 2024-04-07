from database.models.components.base_models import BaseModel
from peewee import CharField


class User(BaseModel):
    email = CharField(unique=True)
    password = CharField()
