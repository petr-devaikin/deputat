from peewee import *

database = SqliteDatabase(None)

class Convocation(Model):
    number = IntegerField()
    start_year = IntegerField()
    stop_year = IntegerField()

    class Meta:
        database = database


class Party(Model):
    name = CharField()

    class Meta:
        database = database


class Fraction(Model):
    convocation = ForeignKeyField(Convocation, related_name='fractions')
    party = ForeignKeyField(Party, related_name='fractions')

    class Meta:
        database = database


class Deputy(Model):
    name = CharField()

    class Meta:
        database = database


class Work(Model):
    deputy = ForeignKeyField(Deputy, related_name='works')
    fraction = ForeignKeyField(Fraction, related_name='fractions')

    class Meta:
        database = database