from peewee import Model, CharField, TimestampField, PrimaryKeyField
from database.database import db

class Users(Model):
    id = PrimaryKeyField()
    name = CharField(max_length=100)
    password = CharField(max_length=255) 
    email = CharField(max_length=100, null=True)

    class Meta:
        database = db
        table_name = 'users'