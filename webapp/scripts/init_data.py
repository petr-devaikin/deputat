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
    lower_name = name.lower()
    if lower_name == "фракция «единая россия»" or lower_name == "ер" or lower_name == "единая россия"
        return "Единая Россия"
    elif lower_name == "фракция «кпрф»" or lower_name == "фракция кпрф" or lower_name == "кпрф"
        return "КПРФ"
    elif lower_name == "фракция «справедливая россия»" or lower_name == "ср"
        return "Справедливая Россия"
    elif lower_name == "фракция «лдпр»" or lower_name == "фракция лдпр" or lower_name == "лдпр"
        return "ЛДПР"
    elif lower_name == "ябл"
        return "Яблоко"
    elif lower_name == "апр"
        return "Аграрная партия России"
    elif lower_name == "агр"
        return "Аграрная депутатская группа"
    elif lower_name == "вр"
        return "Выбор России"
    elif lower_name == "дпр"
        return "Демократическая партия России"
    elif lower_name == "жр"
        return "Женщины России"
    elif lower_name == "н-96"
        return "Новая региональная политика — Дума-96"
    elif lower_name == "нез."
        return "Независимые"
    elif lower_name == "прес"
        return "Партия российского единства и согласия"
    elif lower_name == "росс"
        return "Россия"
    elif lower_name == "стаб"
        return "Стабильность"
    elif lower_name == "ндр"
        return "Наш дом — Россия"
    elif lower_name == "нрдв"
        return "Народовластие"
    elif lower_name == "ррег"
        return "Российские регионы"
    elif lower_name == "апг"
        return "Агропромышленная депутатская группа"
    elif lower_name == "е-ер"
        return "Единство — Единая Россия"
    elif lower_name == "ндеп"
        return "Народный депутат"
    elif lower_name == "о-ер"
        return "Отечество — Единая Россия"
    elif lower_name == "ррос"
        return "Регионы России"
    elif lower_name == "рнвс"
        return "Родина"
    elif lower_name == "ср-р"
        return "Справедливая Россия — Родина"
    else
        return name;


def load_convocation(file_path, convocation):
    f = open(file_path, 'r')
    for line in f:
        s = line.split(';')
        if len(s) >= 2:
            deputy = Deputy.get_or_create(name=s[0])
            party = Party.get_or_create(name=convert_party_name(s[1]))
            fraction = Fraction.get_or_create(convocation=convocation, party=party)
            Work.create(deputy=deputy, fraction=fraction)


def load_all_convocations(data_folder):
    for c in Convocation.query.select():
        file_path = os.path.join(data_folder, "%d.txt" % (c.start_year))
        load_convocation(file_path, c)
