from etr.wsgi import *
import hashlib
import os
import random
import string
import json
import sys

from terem.models import Terem
from kurzus.models import Kurzus
from user.models import Hallgato
from kepzes.models import Kepzes
from elofeltetel.models import Elofeltetel

hallgatok = list(Hallgato.objects.values_list('azonosito', flat=True))
kepzesek = list(Kepzes.objects.values_list('kepzesid', flat=True))
print(hallgatok)
print(kepzesek)

def makeHallgato():

    hallgato = random.choice(hallgatok)
    hallgatok.remove(hallgato)

    return hallgato


def makeKepzes():

    return random.choice(kepzesek)



def makeTeljesitette():

    for i in range(1,300):

        hallgato = makeHallgato()
        kepzes = makeKepzes()

        parancs = f"INSERT INTO felvette (hallgatoAzonosito, kepzesId, teljesitette) VALUES ('{hallgato}', '{kepzes}', {0});"


        with open("felvette.txt", 'a') as file:
            file.writelines(parancs + "\n")


