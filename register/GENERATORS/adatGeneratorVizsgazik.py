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
    legutobbiVizsgaIdopontja = None

    evszam = Kurzustfelvesz.objects.filter(hallgatoAzonosito__azonosito=azonosito).values_list("evszam", flat=True).first() # melyik évben vette fel a kurzust
    legutobbiVizsgaIdopontja = None

    try:
        legutobbiVizsgaIdopontja = Vizsgazik.objects.values_list('vizsgaID__idopont', flat=True).filter(vizsgaID__kurzusKod=kurzusKod, hallgatoAzonosito__azonosito=azonosito).order_by('-vizsgaID__idopont').first()
        legutobbiVizsgaJegye = Vizsgazik.objects.values_list('kapottjegy', flat=True).filter(vizsgaID__kurzusKod=kurzusKod, hallgatoAzonosito__azonosito=azonosito).order_by('-vizsgaID__idopont').first()

        felvehetoVizsgak = Vizsgazik.objects.filter(vizsgaID__kurzusKod=kurzusKod, vizsgaID__idopont__year=evszam ,vizsgaID__idopont__gt=legutobbiVizsgaIdopontja) | Vizsgazik.objects.filter(vizsgaID__kurzusKod=kurzusKod, vizsgaID__idopont__year=evszam+1, vizsgaID__idopont__month__lte=11 ,vizsgaID__idopont__gt=legutobbiVizsgaIdopontja)              #visszaadja a felveheto vizsgakat

    except:
        if legutobbiVizsgaIdopontja is None:
            felvehetoVizsgak = Vizsga.objects.filter(kurzusKod=kurzusKod, idopont__year=evszam)

    try:
        if(legutobbiVizsgaJegye > 1):  # ha már átment a vizsgán akkor kilép
            return False, False
    except:
        try:
            felvettVizsgaID = (random.choice(felvehetoVizsgak.values_list('vizsgaID', flat=True)))   # ha nem akkor már felvette
        except: return False, False


    szamlalo = len(Vizsgazik.objects.filter(vizsgaID__kurzusKod=kurzusKod, hallgatoAzonosito=azonosito))



    alkalom = szamlalo + 1

    if alkalom < 4: # ha több mint 3x kilép
        try:
            return alkalom, felvettVizsgaID   # visszaadja az újonnan felvett vizsgát és hogy hanyadikra vette fel
        except:
            return False, False
    else:
        return False, False


def makeVizsgazik():

        for i in range(1,6000):
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
            print(f"{i}  {parancs}")

            vizsgaObject = Vizsga.objects.get(vizsgaID=vizsgaID)
            hallgatoObject = Hallgato.objects.get(azonosito=hallgatoAzonosito)


            # NEM SZABAD KIKOMMENTEZNI EZT A SORT MERT AKKOR NEM FOG JÓ ADATOT GENERÁLNI
            Vizsgazik.objects.create(vizsgaID=vizsgaObject, hallgatoAzonosito=hallgatoObject, kapottjegy=jegy, vizsgaalkalom=alkalom)

            with open("vizsgazik.txt", 'a') as file:
                file.writelines(parancs + "\n")




makeVizsgazik()

