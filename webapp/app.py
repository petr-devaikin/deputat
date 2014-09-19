# -*- coding: utf-8 -*-
from flask import Flask, render_template
from webapp.db_engine import database, init_db
from webapp.models import Deputy, Party, Fraction, Work, Convocation
import json
from peewee import fn

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
    convocations = {}
    for c in Convocation.select().order_by(Convocation.start_year):
        convocations[c.id] = {
            'id': c.id,
            'start': c.start_year,
            'stop': c.stop_year
        }

    parties = {}
    for p in Party.select():
        parties[p.id] = {
            'id': p.id,
            'name': p.name
        }

    fractions = {}
    for f in Fraction.select():
        fractions[f.id] = {
            'id': f.id,
            'party_id': f.party.id,
            'convocation_id': f.convocation.id,
            'previous_fractions_count': f.order,
            'previous_deputies_count': f.convocation.fractions.join(Work).where(Fraction.order < f.order).count(),
            'deputies_count': f.works.count()
        }

    deputies = {}
    for d in Deputy.select():
        works = []
        for w in d.works.join(Fraction).join(Convocation).order_by(Convocation.start_year):
            works.append({
                'fraction_id': w.fraction.id,
                'previous_deputies_count': w.order
            })
        deputies[d.id] = {
            'name': d.name,
            'works': works
        }

    return render_template('index.html',
        convocations=json.dumps(convocations),
        parties=json.dumps(parties),
        fractions=json.dumps(fractions),
        deputies=json.dumps(deputies))

if __name__ == '__main__':
    init_db()
    app.run()