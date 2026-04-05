from peewee import CharField, BooleanField, DateTimeField, ForeignKeyField
from app.database import BaseModel
from app.models.user import User

class Url(BaseModel):
    user = ForeignKeyField(User, backref='urls')
    short_code = CharField(unique=True)
    original_url = CharField()
    title = CharField()
    is_active = BooleanField(default=True)
    created_at = DateTimeField()
    updated_at = DateTimeField()