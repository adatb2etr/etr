from etr.wsgi import *
from django.contrib.auth.models import User
from tartozas.models import Tartozas

def functioon():

    users = User.objects.all();

    for x in users:

        if x.username != "tesztadmin":
            x.delete()