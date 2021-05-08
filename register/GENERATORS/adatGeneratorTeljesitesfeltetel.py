from etr.wsgi import *
import random
import sys
from kurzus.models import Kurzus
from kepzes.models import Kepzes
from kurzustfelvesz.models import Kurzustfelvesz

kepzesek = list(Kepzes.objects.values_list("kepzesid", flat=True))
kurzusok = list(Kurzus.objects.values_list("kurzuskod", flat=True))


def makeKepzes():

    kepzes = random.choice(kepzesek)
    kepzesek.remove(kepzes)

    return kepzes


def makeKurzusok(kepzes):

    kepzesekLista = []

    for x in kurzusok:
        if kepzes == "SZTE-GAZDINF":
            if not x == "MAT-295":
                kepzesekLista.append(x)

        elif kepzes == "SZTE-PROGTERV":
            if not x == "MAT-286":
                kepzesekLista.append(x)

        elif kepzes == "SZTE-UZEM":
            if not x == "INF-274":
                kepzesekLista.append(x)
        elif kepzes == "SZTE-VILLAMOS":
            if not x == "INF-164":
                kepzesekLista.append(x)
        elif kepzes == "SZTE-MERNOKINF":
            if not x == "INF-233":
                kepzesekLista.append(x)

    return kepzesekLista


def makeTeljesitesFeltetel():

    for i in range (1, 100):
        kepzes = makeKepzes()
        kurzusok = makeKurzusok(kepzes)

        for elem in kurzusok:

            parancs = f"INSERT INTO teljesitesfeltetel (kepzesId, kurzusKod) VALUES ('{kepzes}', '{elem}');"
            print(f"{i} {parancs}")


            with open("teljesitesfeltetel.txt", 'a') as file:
                file.writelines(parancs + "\n")



