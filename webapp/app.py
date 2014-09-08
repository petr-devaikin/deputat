# -*- coding: utf-8 -*-
from flask import Flask, render_template
from webapp.db_engine import database, init_db

app = Flask(__name__)
app.config.from_object('webapp.default_settings')

@app.before_request
def before_request():
    database.connect()

@app.after_request
def after_request(response):
    database.close()
    return response


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    init_db()
    app.run()