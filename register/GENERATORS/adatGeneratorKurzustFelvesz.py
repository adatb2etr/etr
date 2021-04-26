from etr.wsgi import *
import hashlib
import os
import random
import string
import json
import sys
import itertools
from kurzus.models import Kurzus
from user.models import Hallgato
from kurzustfelvesz.models import Kurzustfelvesz

hallgatok = list(Hallgato.objects.values_list("azonosito", flat=True))
kurzusok = list(Kurzus.objects.values_list("kurzuskod", flat=True))


def makeHallgato():

    try:
        hallgatoId = random.choice(hallgatok)
        hallgatok.remove(hallgatoId)
        return hallgatoId
    except:
        return False

def makeAlapKurzusok():

    kurzusokLista = ["MAT-172", "INF-164", "INF-155", "MAT-258", "MAT-289", "INF-222"]

    return kurzusokLista

def makeKurzustFelvesz():

    for i in range(1,400):
        hallgato = makeHallgato()
        if hallgato == False:
            sys.exit()

        hallgatoObject = Hallgato.objects.get(azonosito=hallgato)
        kurzusokLista = makeAlapKurzusok()

        for x in kurzusokLista:
            kurzusObject = Kurzus.objects.get(kurzuskod=x)

            randomszam = random.randint(1, 6)

            if randomszam == 1:
                atment = 0
            else:
                atment = 1

            parancs = f"INSERT INTO kurzustfelvesz (hallgatoAzonosito, kurzuskod, teljesitette) VALUES ('{hallgato}', " \
                      f" '{x}', {atment});"
            print(f"{i} {parancs}")

        #   Kurzustfelvesz.objects.create(hallgatoAzonosito=hallgatoObject, kurzusKod=kurzusObject, teljesitette=atment)

            with open("kurzustfelvesz.txt", 'a') as file:
                file.writelines(parancs + "\n")



