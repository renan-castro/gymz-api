from peewee import Model, CharField, IntegerField, TimestampField
from database.database import db

class Exercices(Model):
    name = CharField(max_length=100)
    series = IntegerField(null=False)
    repeats = IntegerField(null=False)
    days = CharField(null=True)

    class Meta:
        database = db
        table_name = 'exercices'