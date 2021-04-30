from etr.wsgi import *
import hashlib
import os
import random
import string
import json
import sys

from user.models import Hallgato
from tartozas.models import Tartozas

hallgatok = Tartozas.objects.values_list('hallgatoAzonosito', flat=True).filter(tartozasosszeg__gt=0)

def makeTartozasKiegyenlites():

    for x in hallgatok:

        tartozasosszeg = Tartozas.objects.values_list('tartozasosszeg').filter(hallgatoAzonosito__azonosito=x)

