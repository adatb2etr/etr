from etr.wsgi import *
from django.contrib.auth.models import User
from tartozas.models import Tartozas
from user.models import Oktato
from django.contrib.auth.hashers import make_password

def functioon():

    oktatok = Oktato.objects.all()

    for oktato in oktatok:
        User.objects.create(username=oktato.azonosito, first_name=oktato.keresztnev,
                            last_name=oktato.vezeteknev
                            , email=oktato.email, password=make_password(oktato.azonosito))


