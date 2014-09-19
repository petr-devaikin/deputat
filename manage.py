# -*- coding: utf-8 -*-
from flask.ext.script import Manager
from webapp.app import app
from webapp.db_engine import init_db
from webapp.logger import get_logger
from webapp.scripts.create_db import create_db
from webapp.scripts.init_data import init_data, set_order

init_db()
manager = Manager(app)

@manager.command
def hello():
    """
    Print hello
    """
    get_logger().debug("Hello debug")
    get_logger().info("Hello info")
    get_logger().warning("Hello warning")
    get_logger().error("Hello error")
    get_logger().critical("Hello critical")
    print "hello"

@manager.command
def init_db():
    """
    Drop and create database
    """
    create_db()
    init_data('./data/')

@manager.command
def sort():
    """
    Sort fractions and deputies
    """
    set_order()

if __name__ == "__main__":
    manager.run()
