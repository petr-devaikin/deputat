# -*- coding: utf-8 -*-
from flask import Flask
from webapp.db_engine import database, init_db

app = Flask(__name__)
app.config['DEBUG'] = True

@app.before_request
def before_request():
    database.connect()

@app.after_request
def after_request(response):
    database.close()
    return response


@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    init_db()
    app.run()