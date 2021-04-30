from etr.wsgi import *
import hashlib
import os
import random
import string
import json
import sys

felhasznaltAzonositok = []

def makeName():
    random.seed = (os.urandom(1024))
    names = json.loads(open('names.json').read())

    vezeteknev = random.choice(names)
    keresztnev = random.choice(names)

    return vezeteknev, keresztnev


def makeAzonosito():

    chars = string.ascii_uppercase + string.digits

    while True:
        id = "".join(random.choice(chars) for i in range(6))
        if id not in felhasznaltAzonositok:
            felhasznaltAzonositok.append(id)
            return id

def makeSzemelyi():

    chars = string.ascii_uppercase + string.digits
    szemelyiszam = "".join(random.choice(chars) for i in range(8))

    return szemelyiszam

def makeTelefonszam():
    chars = string.digits
    szolgaltato = ["20", "30", "70"]
    tfonszam = "+36" + (random.choice(szolgaltato))
    tfonszamVege = "".join(random.choice(chars) for i in range(7))

    tfonszam = tfonszam+tfonszamVege

    return tfonszam

def makeEmail(keresztnev):

    chars = string.ascii_letters + string.digits
    random.seed = (os.urandom(1024))

    name_extra = ''.join(random.choice(chars)for i in range(4))

    email = keresztnev + name_extra + "@" + "gmail.com"

    return email

def makeJelszo(azonosito):

    encryptedJelszo = (hashlib.sha256(azonosito.encode())).hexdigest()
    return encryptedJelszo


def makeSzulido():

    ev = random.randint(1960, 2002)
    honap = random.randint(1, 12)

    naposok31 = [1,3,5,7,8,10,12]
    naposok30 = [4,6,9,11]

    if honap in naposok31:
        nap = random.randint(1,31)
    elif honap in naposok30:
        nap = random.randint(1,30)
    elif honap == 2:
        nap = random.randint(1,28)
    else:
        nap = 10

    if honap < 10 :
        honap = "0"+str(honap)
    if nap < 10:
        nap = "0"+str(nap)

    return f"{ev}-{honap}-{nap}"


def makeHallgatok():

    for i in range(1, 200):
        azonosito = makeAzonosito()
        vezeteknev, keresztnev = makeName()
        szemelyiszam = makeSzemelyi()
        telefonszam = makeTelefonszam()
        email = makeEmail(keresztnev)
        jelszo = makeJelszo(keresztnev)
        szulido = makeSzulido()

        parancs = f"INSERT INTO hallgato VALUES ('{azonosito}', '{vezeteknev}', '{keresztnev}', '{szemelyiszam}', '{telefonszam}'" \
                  f", '{email}', '{jelszo}', TO_DATE('{szulido}', 'yyyy-mm-dd'));"

        print (parancs)

        with open ("hallgatok.txt", 'a') as file:

            file.writelines(parancs + "\n")

def makeOktato():

    for i in range(1, 20):
        azonosito = makeAzonosito()
        vezeteknev, keresztnev = makeName()
        szemelyiszam = makeSzemelyi()
        telefonszam = makeTelefonszam()
        email = makeEmail(keresztnev)
        jelszo = makeJelszo(keresztnev)
        szulido = makeSzulido()

        parancs = f"INSERT INTO oktato VALUES ('{azonosito}', '{vezeteknev}', '{keresztnev}', '{szemelyiszam}', '{telefonszam}'" \
                  f", '{email}', '{jelszo}', TO_DATE('{szulido}', 'yyyy-mm-dd'));"

        print(parancs)

        with open("oktatok.txt", 'a') as file:
            file.writelines(parancs + "\n")



