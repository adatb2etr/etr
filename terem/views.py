from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from django.db import connection
from terem.forms import TeremForm, TeremFormUpdate
from terem.models import Terem
from user.validators.validators import is_EtrAdmin
from django.shortcuts import redirect
from django.shortcuts import render
from idopont.models import Idopont
import datetime
from kurzus.models import Kurzus
from kurzustfelvesz.models import Kurzustfelvesz
kurzusok = list(Kurzus.objects.values_list('kurzuskod', flat=True))
termek  = list(Kurzus.objects.values_list('teremCim__cim', flat=True))
evszamok = list(set(Kurzustfelvesz.objects.values_list('evszam', flat=True)))


def terem_create_view(request):

    if is_EtrAdmin(request):
        if is_EtrAdmin(request) is True:
            form = TeremForm(request.POST or None)
            if form.is_valid():
                form.save()
                form = TeremForm()

            context = {
                'obj' : form
            }

            return render(request, 'terem_creation.html', context)


def terem_update_view(request, terem_cim):
    if is_EtrAdmin(request):
        obj = get_object_or_404(Terem, cim=terem_cim)
        form = TeremFormUpdate(request.POST or None, instance=obj)
        if form.is_valid():
            form.save()
            return redirect("../../../termek/")
        context = {
            'obj' : form
        }
        return render(request, "terem_creation.html", context)

def terem_lookup_view(request, terem_cim):
    obj = get_object_or_404(Terem, cim=terem_cim)

    context = {
        "obj": obj
    }
    return render(request, "terem_detail.html", context)

def terem_delete_view(request, terem_cim):
    if is_EtrAdmin(request):
        obj = get_object_or_404(Terem, cim=terem_cim)
        if request.method == "POST":
            obj.delete()
            return redirect("../../../termek/")
        context = {
            "obj": obj
        }
        return render(request, "terem_delete.html", context)


def terem_list_view(request):
    queryset = Terem.objects.all()  #list of objects
    context = {
        "object_list": queryset
    }
    return render(request, "terem_list.html", context)





class TeremKihasznaltsagStat(TemplateView):
    template_name = 'teremkihasznaltsag.html'

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




    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['evszamok'] = self.evszamList
        context['kurzusok'] = termek
        context['felvettek'] = self.felvettekLista   # [[53,41,37,38,30], [20,20,20,20,20,20], ...]


        return context