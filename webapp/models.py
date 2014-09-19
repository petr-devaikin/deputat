# -*- coding: utf-8 -*-
from peewee import *
from webapp.db_engine import database

class Convocation(Model):
    number = IntegerField(unique=True)
    start_year = IntegerField(unique=True)
    stop_year = IntegerField(unique=True)

    class Meta:
        database = database


class Party(Model):
    name = CharField(unique=True)

    class Meta:
        database = database


class Fraction(Model):
    convocation = ForeignKeyField(Convocation, related_name='fractions')
    party = ForeignKeyField(Party, related_name='fractions')
    order = IntegerField(null=True)

    class Meta:
        database = database
        indexes = (
            (('convocation', 'party'), True),
            (('convocation', 'order'), True),
        )


class Deputy(Model):
    name = CharField(unique=True)

    class Meta:
        database = database


class Work(Model):
    deputy = ForeignKeyField(Deputy, related_name='works')
    fraction = ForeignKeyField(Fraction, related_name='works')
    order = IntegerField(null=True)

    class Meta:
        database = database
        indexes = (
            (('fraction', 'deputy'), True),
            (('fraction', 'order'), True),
        )