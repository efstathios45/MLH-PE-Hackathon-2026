from peewee import CharField, DateTimeField, TextField, ForeignKeyField
from app.database import BaseModel
from app.models.user import User
from app.models.url import Url

class Event(BaseModel):
    url = ForeignKeyField(Url, backref='events')
    user = ForeignKeyField(User, backref='events')
    event_type = CharField()
    timestamp = DateTimeField()
    details = TextField() # Storing the JSON details as text