import sys

from etr.wsgi import *
import hashlib
import os
import random
import string
import json
import datetime
from kurzus.models import Kurzus
from idopont.models import Idopont

felhasznaltKezdoIdopontok = []

kurzuskodok = list(Kurzus.objects.values_list('kurzuskod', flat=True))

def makeIdopontok():

    lehetsegesKezdoorak = [8,10,12,14,16,18]
    lehetsegeskezdoDatumokSzeptemberre = [1,2,3,4,7]

    lehetsegesKezdoIdopontok = []

    for x in lehetsegeskezdoDatumokSzeptemberre:
        for y in lehetsegesKezdoorak:
            felhasznaltIdopont = str(x) + str(y)
            lehetsegesKezdoIdopontok.append(felhasznaltIdopont)

    while True:
        if all(elem in felhasznaltKezdoIdopontok for elem in lehetsegesKezdoIdopontok):
            return False
        else:
            kezdoIdopont = random.choice(lehetsegesKezdoIdopontok)
            if kezdoIdopont not in felhasznaltKezdoIdopontok:
                felhasznaltKezdoIdopontok.append(kezdoIdopont)

                day = int(kezdoIdopont[0])
                hour = int(kezdoIdopont[1:])
                idopont = datetime.datetime(year=2020, month=9, day=day, hour=hour, minute=0, microsecond=0)

                idopontokKezdete = []
                idopontokVege = []
                for i in range(1,15):
                    ujidopontKezdete = idopont + datetime.timedelta(days=(i*7 - 7))
                    ujidopontVege = ujidopontKezdete + datetime.timedelta(minutes=90)

                    idopontokKezdete.append(ujidopontKezdete)
                    idopontokVege.append(ujidopontVege)

                idopontLista = list(zip(idopontokKezdete, idopontokVege))
                return idopontLista

def makeKurzus():

    try:
        kurzus = random.choice(kurzuskodok)
        kurzuskodok.remove(kurzus)
    except:
        return None

    return kurzus



def makeIdopont():

    for i in range (1,100):
        idopontLista = makeIdopontok()

        if idopontLista == None:
            sys.exit()

        kurzusKod = makeKurzus()

        if kurzusKod == None:
            sys.exit()


        for idopont in idopontLista:
            parancs = f"INSERT INTO idopont (kezdete, vege, kurzusKod) VALUES (TO_DATE('{idopont[0]}', 'yyyy-mm-dd HH24:MI:SS')," \
                      f" TO_DATE('{idopont[1]}', 'yyyy-mm-dd HH24:MI:SS'), '{kurzusKod}');"

            kurzusObject = Kurzus.objects.get(kurzuskod=str(kurzusKod))
            Idopont.objects.create(kezdete=idopont[0], vege=idopont[1], kurzusKod=kurzusObject)

            with open("idopontok.txt", 'a') as file:
                file.writelines(parancs + "\n")


