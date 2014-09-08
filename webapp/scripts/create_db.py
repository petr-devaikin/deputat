# -*- coding: utf-8 -*-
from webapp.logger import get_logger
from webapp.models import *


def drop_tables():
    if Work.table_exists():
        Work.drop_table()
        get_logger().debug('Work table dropped')
        
    if Deputy.table_exists():
        Deputy.drop_table()
        get_logger().debug('Deputy table dropped')
        
    if Fraction.table_exists():
        Fraction.drop_table()
        get_logger().debug('Fraction table dropped')
        
    if Party.table_exists():
        Party.drop_table()
        get_logger().debug('Party table dropped')
        
    if Convocation.table_exists():
        Convocation.drop_table()
        get_logger().debug('Convocation table dropped')


def create_tables():
    Convocation.create_table()
    get_logger().debug('Convocation table created')

    Party.create_table()
    get_logger().debug('Party table created')

    Fraction.create_table()
    get_logger().debug('Fraction table created')

    Deputy.create_table()
    get_logger().debug('Deputy table created')

    Work.create_table()
    get_logger().debug('Work table created')
    

def create_db():
    drop_tables()
    create_tables()