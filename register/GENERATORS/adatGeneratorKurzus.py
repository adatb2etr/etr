from etr.wsgi import *
import hashlib
import os
import random
import string
import json
import sys

from terem.models import Terem
from kurzus.models import Kurzus
from user.models import Oktato
from elofeltetel.models import Elofeltetel

termek = Terem.objects.values_list('cim', flat=True)
oktatok = Oktato.objects.values_list('azonosito', flat=True)

felhasznaltAzonositok = []
felhasznaltNevek = []

def makeKurzusKod():

    kurzusprefixek = ["INF", "MAT"]
    kodszam = random.randint(100,350)

    while True:
        id = random.choice(kurzusprefixek) + "-" + str(kodszam)
        if id not in felhasznaltAzonositok:
            felhasznaltAzonositok.append(id)
            return id

def makeKurzusNev(kurzusKod):

    nevekMatekhoz = ["Algoritmusok 1", "Algoritmusok 2", "Diszkrét Matek 1", "Diszkrét Matek 2", "Kalkulus 1", "Kalkulus 2"]
    nevekProghoz = ["Programozás Alapjai", "Programozás 1", "Programozás 2", "Szkriptnyelvek", "Prognyelvek", "Assembly"]


    if all(elem in felhasznaltNevek for elem in nevekMatekhoz) and all(elem in felhasznaltNevek for elem in nevekProghoz):
        sys.exit()

    if kurzusKod.startswith("INF"):
        if not all(elem in felhasznaltNevek for elem in nevekProghoz):
            while True:
                kurzusnev = random.choice(nevekProghoz)
                if kurzusnev not in felhasznaltNevek:
                    felhasznaltNevek.append(kurzusnev)
                    return kurzusnev

    if kurzusKod.startswith("MAT"):
        if not all(elem in felhasznaltNevek for elem in nevekMatekhoz):
            while True:
                kurzusnev = random.choice(nevekMatekhoz)
                if kurzusnev not in felhasznaltNevek:
                    felhasznaltNevek.append(kurzusnev)
                    return kurzusnev

    return False

def makeTeremCim():

    return (random.choice(termek))

def makeFerohely():
    return 0

def makeKredit():
    return random.randint(1,5)

def makeOktato():
    return random.choice(oktatok)

def makeMeghirdetett():
    return 0


def makeKurzus():

    for i in range (1,100):
        kurzuskod = makeKurzusKod()
        kurzusnev = makeKurzusNev(kurzuskod)
        if kurzusnev == False:
            continue
        ferohely = makeFerohely()
        kredit = makeKredit()
        teremcim = makeTeremCim()
        oktatoAzonosito = makeOktato()
        meghirdetett = makeMeghirdetett()

        teremObject = Terem.objects.get(cim=teremcim)
        oktatoObject = Oktato.objects.get(azonosito=oktatoAzonosito)
        Kurzus.objects.create(kurzuskod=kurzuskod, kurzusnev=kurzusnev, ferohely=ferohely, kredit=kredit,
                              teremCim=teremObject, oktatoAzonosito=oktatoObject, meghirdetett=meghirdetett)

        parancs = f"INSERT INTO kurzus VALUES ('{kurzuskod}', '{kurzusnev}', '{ferohely}', '{kredit}', '{teremcim}'" \
                  f", '{oktatoAzonosito}', '{meghirdetett}');"

        with open("kurzusok.txt", 'a') as file:
            file.writelines(parancs + "\n")


## egyedül ezeket kell kézzel beírni
def makeElofeltetel():

    mat268 = Kurzus.objects.get(kurzuskod="MAT-268")
    inf233 = Kurzus.objects.get(kurzuskod="INF-233")
    inf274 = Kurzus.objects.get(kurzuskod="INF-274")
    mat295 = Kurzus.objects.get(kurzuskod="MAT-295")
    mat286 = Kurzus.objects.get(kurzuskod="MAT-286")
    inf199 = Kurzus.objects.get(kurzuskod="INF-199")

    mat172 = Kurzus.objects.get(kurzuskod="MAT-172")
    inf199 = Kurzus.objects.get(kurzuskod="INF-199")
    inf155 = Kurzus.objects.get(kurzuskod="INF-155")
    mat289 = Kurzus.objects.get(kurzuskod="MAT-289")
    mat258 = Kurzus.objects.get(kurzuskod="MAT-258")
    inf155 = Kurzus.objects.get(kurzuskod="INF-155")

    Elofeltetel.objects.create(kurzusKod=mat268, elofeltetelKod=mat172)
    Elofeltetel.objects.create(kurzusKod=inf233, elofeltetelKod=inf199)
    Elofeltetel.objects.create(kurzusKod=inf274, elofeltetelKod=inf155)
    Elofeltetel.objects.create(kurzusKod=mat295, elofeltetelKod=mat289)
    Elofeltetel.objects.create(kurzusKod=mat286, elofeltetelKod=mat258)
    Elofeltetel.objects.create(kurzusKod=inf199, elofeltetelKod=inf155)
