from etr.wsgi import *
import hashlib
import os
import random
import string
import json
import sys
import itertools
from terem.models import Terem

felhasznaltCimek = []
lehetsegesKapacitasok = [20, 30, 50, 70, 600]

def makeKapacitas():

    kapacitas = random.choice(lehetsegesKapacitasok)
    if kapacitas == 600:
        lehetsegesKapacitasok.remove(600)
    return kapacitas

def makeCim():

    lehetsegesSzobaszamok = ["01","02","03","04","05"]
    lehetsegesSzintek = ["1","2","3"]

    lehetsegesCimek = []
    for x in lehetsegesSzobaszamok:
        for y in lehetsegesSzintek:
            cim = y + x
            lehetsegesCimek.append(cim)


    while True:
        if all(elem in felhasznaltCimek for elem in lehetsegesCimek):
            return False
        else:
            cim = random.choice(lehetsegesCimek)
            if cim not in felhasznaltCimek:
                felhasznaltCimek.append(cim)
                return f"{cim[0]}.emelet {cim} Terem"

def makeTerem():

    for i in range (1,101):
        kapacitas = makeKapacitas()
        cim = makeCim()
        if cim == False:
            sys.exit()
        parancs = f"INSERT INTO terem VALUES ('{cim}', {kapacitas});"
        Terem.objects.create(cim=cim, kapacitas=kapacitas)
        with open("termek.txt", 'a') as file:
            file.writelines(parancs + "\n")
