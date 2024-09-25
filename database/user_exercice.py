from peewee import *
from database.database import db
from database.exercice import Exercices
from database.user import Users

class UserExercices(Model):
    user = ForeignKeyField(Users, backref='user')
    exercice = ForeignKeyField(Exercices, backref='user_exercices')

    class Meta:
        database = db
        table_name = 'exercices'
