from etr.wsgi import *
import random
import sys
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


def makeEvszam(hallgatoAzonosito):

    evszam = Kurzustfelvesz.objects.filter(hallgatoAzonosito=hallgatoAzonosito).values_list("evszam", flat=True).first()

    if evszam is None or evszam == 0:
        evszam = random.randint(2016, 2020)

    return evszam

def checkTeremkapacitas(kurzusObject, evszam):

    maxKapacitas = kurzusObject.teremCim.kapacitas
    felvettek = len(Kurzustfelvesz.objects.filter(kurzusKod=kurzusObject).filter(evszam=evszam))

    if felvettek < maxKapacitas:
        return True
    else:
        return False

def makeKurzustFelvesz():

    for i in range(1,400):
        hallgato = makeHallgato()
        if hallgato == False:
            sys.exit()

        evszam = makeEvszam(hallgato)
        hallgatoObject = Hallgato.objects.get(azonosito=hallgato)
        kurzusokLista = makeAlapKurzusok()

        for x in kurzusokLista:
            kurzusObject = Kurzus.objects.get(kurzuskod=x)
            if checkTeremkapacitas(kurzusObject, evszam) is True:

                randomszam = random.randint(1, 6)

                if randomszam == 1:
                    atment = 0
                else:
                    atment = 1

                parancs = f"INSERT INTO kurzustfelvesz (hallgatoAzonosito, kurzuskod, teljesitette, evszam) VALUES ('{hallgato}', " \
                          f" '{x}', {atment}, {evszam});"
                print(f"{i} {parancs}")

                # NEM SZABAD KIKOMMENTEZNI EZT A SORT MERT AKKOR NEM FOG JÓ ADATOT GENERÁLNI
                Kurzustfelvesz.objects.create(hallgatoAzonosito=hallgatoObject, kurzusKod=kurzusObject, teljesitette=atment, evszam=evszam)

                with open("kurzustfelvesz.txt", 'a') as file:
                    file.writelines(parancs + "\n")

