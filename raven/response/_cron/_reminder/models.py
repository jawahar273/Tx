from datetime import datetime

from walrus import Model, TextField, IntegerField, DateTimeField

from config.stage import db


class CountdownTracker(Model):
    __database__ = db
    id = TextField(primary_key=True)
    seconds = IntegerField()
    desc = TextField()
    created_at = DateTimeField(default=datetime.now)
