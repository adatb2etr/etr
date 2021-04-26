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
from vizsgazik.models import Vizsgazik
from user.models import Hallgato
from kurzustfelvesz.models import Kurzustfelvesz

hallgatok = Hallgato.objects.values_list("azonosito", flat=True)
kurzusok = Kurzus.objects.values_list("kurzuskod", flat=True)
kurzustfelvesz = Kurzustfelvesz.objects.all()
vizsgak = Vizsga.objects.all()



def makeHallgato():

    hallgatoID = random.choice(hallgatok)

    return hallgatoID


def makeKurzusPlusszJegy(hallgatoID):

    felvettKurzusokLista = Kurzustfelvesz.objects.filter(hallgatoAzonosito=hallgatoID)

    kurzusIDk = []
    teljesitesek = []

    for x in felvettKurzusokLista:
        kurzusCIM = x.kurzusKod # kurzus objectet visszaadja
        teljesit = x.teljesitette
        kurzusIDk.append(kurzusCIM)
        teljesitesek.append(teljesit)

    teljesitette = list(zip(kurzusIDk, teljesitesek))
    kurzusForReturn = random.choice(teljesitette)

    return kurzusForReturn[0], kurzusForReturn[1]


def makeAlkalom(azonosito, kurzusKod):

    szamlalo = 0

    vizsgak = Vizsga.objects.filter(kurzusKod=kurzusKod)

    osszesVizsgaId = []
    felvettVizsgaID = []

    for x in vizsgak:
        osszesVizsgaId.append(x.vizsgaID)
        try:
            vizsgakatFelvett = Vizsgazik.objects.get(vizsgaID=x, hallgatoAzonosito__azonosito=azonosito)

            if(vizsgakatFelvett.kapottjegy > 1):
                return False, False
            felvettVizsgaID.append(x.vizsgaID)
            szamlalo += 1
        except:
            pass

    felnemVettVizsgaIDk = [item for item in osszesVizsgaId if item not in felvettVizsgaID]

    alkalom = szamlalo + 1

    if alkalom < 4:
        return alkalom, random.choice(felnemVettVizsgaIDk)
    else:
        return False, False


def makeVizsgazik():

        for i in range(1,4000):
            hallgatoAzonosito = makeHallgato()
            kurzus, teljesitette = makeKurzusPlusszJegy(hallgatoAzonosito)
            kurzusCime = kurzus.kurzuskod

            alkalom, vizsgaID = makeAlkalom(hallgatoAzonosito, kurzus)

            if alkalom == False:
                continue

            if teljesitette == 0:
                jegy = 1
            elif alkalom == 3 and teljesitette == 1:
                jegy = random.randint(2,5)
            elif teljesitette == 1 and alkalom < 3:
                jegy = random.randint(1,5)



            parancs = f"INSERT INTO vizsgazik (vizsgaID, hallgatoAzonosito, kapottjegy, vizsgaalkalom) VALUES " \
                      f"('{vizsgaID}', " \
                      f"'{hallgatoAzonosito}', {jegy}, {alkalom});"
            print(parancs)

            vizsgaObject = Vizsga.objects.get(vizsgaID=vizsgaID)
            hallgatoObject = Hallgato.objects.get(azonosito=hallgatoAzonosito)

            Vizsgazik.objects.create(vizsgaID=vizsgaObject, hallgatoAzonosito=hallgatoObject, kapottjegy=jegy, vizsgaalkalom=alkalom)

            with open("vizsgazik.txt", 'a') as file:
                file.writelines(parancs + "\n")

            print(i)






