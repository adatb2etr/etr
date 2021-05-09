from django.views.generic import TemplateView

from etr.wsgi import *
from django.contrib.auth.models import User
from tartozas.models import Tartozas
from django.db import connection
from idopont.models import Idopont

def functioon():

    users = User.objects.all();

    for x in users:

        if x.username != "tesztadmin":
            x.delete()




def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]




class TeremKihasznaltsagStat(TemplateView):
    template_name = 'teremkihasznaltsag.html'

    cursor = connection.cursor()
    cursor.execute("SELECT round(avg(vizsgazik.kapottJegy), 2), vizsga.kurzusKod from vizsgazik, vizsga where vizsga.vizsgaID = vizsgazik.vizsgaID group by vizsga.kurzusKod;")
    r = dictfetchall(cursor)

    listIdopontok = []
    listTeremCimek = []

    def print(self):
        for x in self.r:
            print(x)



    """
   def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
        """

valami = TeremKihasznaltsagStat()


from kurzus.models import Kurzus
from kurzustfelvesz.models import Kurzustfelvesz
from terem.models import Terem

kurzusok = list(Kurzus.objects.values_list('kurzuskod', flat=True))
evszamok = list(set(Kurzustfelvesz.objects.values_list('evszam', flat=True)))

def vmi():

    szotar = dict()

    for x in evszamok:
        szotar2 = dict()

        for y in kurzusok:
            szotar2[y] = len(Kurzustfelvesz.objects.filter(evszam=x, kurzusKod__kurzuskod=y))

        szotar[x] = szotar2

    evszamList = szotar.keys()
    felvettekLista = []


    for key, value in szotar.items():
        felvettek2lista = []

        for key2, value2 in value.items():
            felvettek2lista.append(value2)

        felvettekLista.append(felvettek2lista)

    print(szotar)
    print(evszamList)
    print(felvettekLista)




vmi()

