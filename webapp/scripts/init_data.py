# -*- coding: utf-8 -*-
from webapp.models import *
from webapp.logger import get_logger
import os


def create_convocations():
    Convocation.create(number=1, start_year=1993, stop_year=1996)
    Convocation.create(number=2, start_year=1996, stop_year=2000)
    Convocation.create(number=3, start_year=2000, stop_year=2004)
    Convocation.create(number=4, start_year=2004, stop_year=2011)
    Convocation.create(number=5, start_year=2011, stop_year=2016)

    get_logger().debug('Convocations created')


def convert_party_name(name):
    lower_name = unicode(name, 'UTF-8').lower()
    if lower_name == u"фракция «единая россия»" or lower_name == u"ер" or lower_name == u"единая россия":
        return u"Единая Россия"
    elif lower_name == u"фракция «кпрф»" or lower_name == u"фракция кпрф" or lower_name == u"кпрф":
        return u"КПРФ"
    elif lower_name == u"фракция «справедливая россия»" or lower_name == u"ср":
        return u"Справедливая Россия"
    elif lower_name == u"фракция «лдпр»" or lower_name == u"фракция лдпр" or lower_name == u"лдпр":
        return u"ЛДПР"
    elif lower_name == u"ябл":
        return u"Яблоко"
    elif lower_name == u"апр":
        return u"Аграрная партия России"
    elif lower_name == u"агр":
        return u"Аграрная депутатская группа"
    elif lower_name == u"вр":
        return u"Выбор России"
    elif lower_name == u"дпр":
        return u"Демократическая партия России"
    elif lower_name == u"жр":
        return u"Женщины России"
    elif lower_name == u"н-96":
        return u"Новая региональная политика — Дума-96"
    elif lower_name == u"нез.":
        return u"Независимые"
    elif lower_name == u"прес":
        return u"Партия российского единства и согласия"
    elif lower_name == u"росс":
        return u"Россия"
    elif lower_name == u"стаб":
        return u"Стабильность"
    elif lower_name == u"ндр":
        return u"Наш дом — Россия"
    elif lower_name == u"нрдв":
        return u"Народовластие"
    elif lower_name == u"ррег":
        return u"Российские регионы"
    elif lower_name == u"апг":
        return u"Агропромышленная депутатская группа"
    elif lower_name == u"е-ер":
        return u"Единство — Единая Россия"
    elif lower_name == u"ндеп":
        return u"Народный депутат"
    elif lower_name == u"о-ер":
        return u"Отечество — Единая Россия"
    elif lower_name == u"ррос":
        return u"Регионы России"
    elif lower_name == u"рнвс":
        return u"Родина"
    elif lower_name == u"ср-р":
        return u"Справедливая Россия — Родина"
    else:
        return name


def extract_deputy_and_party(line):
    s = line.split(';')
    if len(s) >= 2 and len(s[0]) > 0:
        return (s[0], convert_party_name(s[1]))
    elif len(s) >= 3:
        return (s[1], convert_party_name(s[2]))
    else:
        return None

def load_convocation(file_path, convocation):
    f = open(file_path, 'r')
    for line in f:
        res = extract_deputy_and_party(line)
        if res != None:
            deputy = Deputy.get_or_create(name=res[0])
            party = Party.get_or_create(name=res[1])
            fraction = Fraction.get_or_create(convocation=convocation, party=party)
            Work.create(deputy=deputy, fraction=fraction)

    get_logger().debug('Data from %s loaded' % file_path)


def load_all_convocations(data_folder):
    to_load = []
    for c in Convocation.select():
        to_load.append(c)
    for c in to_load:
        file_path = os.path.join(data_folder, "%d.txt" % (c.start_year))
        load_convocation(file_path, c)


def clear_order():
    for f in Fraction.select():
        f.order = None
        f.save()

    for w in Work.select():
        w.order = None
        w.save()

def set_order():
    clear_order()

    for c in Convocation.select():
        fraction_order = 0

        fractions = []
        for f in c.fractions.join(Party).order_by(Party.name):
            fractions.append(f)

        for f in fractions:
            f.order = fraction_order
            f.save()
            fraction_order += 1
            print "--- ", fraction_order

            work_order = 0
            works = []
            for w in f.works.join(Deputy).order_by(Deputy.name):
                works.append(w)

            for w in works:
                print work_order
                w.order = work_order
                w.save()
                work_order += 1


def init_data(data_folder):
    create_convocations()
    load_all_convocations(data_folder)