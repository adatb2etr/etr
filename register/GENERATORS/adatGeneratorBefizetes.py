from etr.wsgi import *
import hashlib
import os
import random
import string
import json
import sys

from user.models import Hallgato
from tartozas.models import Tartozas
from vizsgazik.models import Vizsgazik


hallgatok = Tartozas.objects.values_list('hallgatoAzonosito', flat=True).filter(tartozasosszeg__gt=0)

def makeTartozasKiegyenlites():

    for x in hallgatok:
        tartozasosszeg = [x for x in Tartozas.objects.values_list('tartozasosszeg', flat=True).filter(hallgatoAzonosito__azonosito=x)]
        tartozasosszeg = tartozasosszeg[0]
        legutobbiVizsgaIdopontja = Vizsgazik.objects.values_list('vizsgaID__idopont', flat=True).filter(
           hallgatoAzonosito__azonosito=x).order_by(
            '-vizsgaID__idopont').first()

        legutobbiVizsgaIdopontja = str(legutobbiVizsgaIdopontja)[:-6]


        parancs = f"INSERT INTO befizetes (hallgatoAzonosito, befizetesosszeg, datum) VALUES " \
                  f"('{x}', " \
                  f"{tartozasosszeg}, TO_DATE('{legutobbiVizsgaIdopontja}', 'yyyy-mm-dd hh24:mi:ss'));"
        print(f"{parancs}")

        with open("befizetes.txt", 'a') as file:
            file.writelines(parancs + "\n")


makeTartozasKiegyenlites()