from peewee import *
from database.database import db
from database.exercice import Exercices
from database.user import Users

class UserExercices(Model):
    user = ForeignKeyField(Users, backref='user_exercices', to_field='id')
    exercice = ForeignKeyField(Exercices, backref='user_exercices', to_field='id')

    class Meta:
        database = db
        table_name = 'user_exercices'
        primary_key = CompositeKey('user', 'exercice')  
