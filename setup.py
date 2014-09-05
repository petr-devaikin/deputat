#!/usr/bin/env python

from setuptools import setup

setup(
    name='Deputat',
    version='1.0',
    description='Russian Duma chart',
    author='Petr Devaikin',
    author_email='p.devaikin@gmail.com',
    include_package_data=True,
    zip_safe=False,
    packages=['webapp'],
    setup_requires=['Flask'],
    install_requires=['Flask', 'peewee', 'Flask-Script', 'MySQL-Python']
)