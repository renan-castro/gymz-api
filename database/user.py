from peewee import Model, CharField, TimestampField
from database.database import db

class Users(Model):
    name = CharField(max_length=100)
    password = CharField(max_length=255) 
    email = CharField(max_length=100, null=True)

    class Meta:
        database = db
        table_name = 'users'
