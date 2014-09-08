# -*- coding: utf-8 -*-
from peewee import *

database = Proxy()

def init_db():
    db = SqliteDatabase('/tmp/deputat.db', threadlocals=True)
    database.initialize(db)