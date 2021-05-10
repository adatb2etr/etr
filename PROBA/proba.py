from etr.wsgi import *
from django.contrib.auth.models import User
from tartozas.models import Tartozas

def functioon():

    users = User.objects.all();

    for x in users:

        if x.username != "tesztadmin":
            x.delete()


def dec_to_bin(x):
    return str(bin(x)[2:])


def modszam(number, exponent, modulus):
    szam = dec_to_bin(exponent)

    print(f"{exponent} kettes számrendszerben: {szam}")
    d = 1
    k = 0

    for i in range(0,len(szam)):
        d = ( d ** 2 ) % modulus
        k += 1
        print(f"{k} dik  után a d : {d}")

        if int(szam[i]) % 2 == 1:
            d = (d * number) % modulus
            k += 1
            print(f"{k} dik  után a d : {d}")

       # print(f"A d értéke az {i}. iteráció után: {d}")

modszam(11,19,17)