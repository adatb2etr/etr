from etr.wsgi import *
import hashlib
import os
import random
import string
import json
import sys
import datetime

from kurzus.models import Kurzus
from terem.models import Terem
from vizsga.models import Vizsga


kurzusok = list(Kurzus.objects.values_list('kurzuskod', flat=True))
termek = list(Terem.objects.values_list('cim', flat=True))

felhasznaltIdopontok = []

def makeKurzusKod():

    try:
        kurzusKod = random.choice(kurzusok)
        kurzusok.remove(kurzusKod)
        return kurzusKod
    except:
        return False

def makeIdopont():

    vizsgaIdopontok = []

    for i in range(1,(random.randint(6,10))):
        flag = False
        while flag == False:
            randomHet = random.randint(0, 7)
            randomNap = random.randint(0, 4)
            randomOra = random.randint(10, 18)


            vizsgaidopont = datetime.datetime(year=2020, month=12, day=14, hour=randomOra, minute=0, second=0, microsecond=0) + datetime.timedelta(weeks=randomHet,days=randomNap)
            if(vizsgaidopont not in felhasznaltIdopontok):
                flag = True
                felhasznaltIdopontok.append(vizsgaidopont)
                vizsgaIdopontok.append(vizsgaidopont)

    return vizsgaIdopontok


def makeFerohely(kurzusKod):

    kurzus = Kurzus.objects.get(kurzuskod=kurzusKod)
    teremCim = kurzus.teremCim.cim
    terem = Terem.objects.get(cim=teremCim)

    ferohely = terem.kapacitas

    return ferohely


def makeVizsga():

    for i in range(1,3000):
        kurzusKod = makeKurzusKod()
        if kurzusKod == False:
            sys.exit()

        ferohely = makeFerohely(kurzusKod)
        idopontok = makeIdopont()

        for idopont in idopontok:
            parancs = f"INSERT INTO vizsga (kurzusKod, idopont, ferohely) VALUES ('{kurzusKod}', " \
                      f"TO_DATE('{idopont}', 'yyyy-mm-dd HH24:MI:SS'), {ferohely});"

            kurzusObject = Kurzus.objects.get(kurzuskod=kurzusKod)
            Vizsga.objects.create(kurzusKod=kurzusObject, idopont=idopont, ferohely=ferohely)

            with open("vizsgak.txt", 'a') as file:
                file.writelines(parancs + "\n")


