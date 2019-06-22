

from walrus import Model, TextField

from config.stage import db


class User(Model):
    __database__ = db
    nickname = TextField(primary_key=True)

