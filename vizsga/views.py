from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from .forms import VizsgaForm
from .models import Vizsga
from user.models import Hallgato
from vizsgatfelvesz.models import VizsgatFelvesz
from user.validators.validators import is_EtrAdmin
from django.shortcuts import redirect
from django.shortcuts import render
from user.validators.queries import getids, getRole, getEtrAdminIds, getHallgatoIds, getOktatoIds
from vizsgazik.models import Vizsgazik
from django.db import connection


def vizsga_create_view(request):

    if is_EtrAdmin(request):
        if is_EtrAdmin(request) is True:
            form = VizsgaForm(request.POST or None)
            if form.is_valid():
                form.save()
                form = VizsgaForm()

            context = {
                'obj' : form
            }

            return render(request, 'vizsga_creation.html', context)


def vizsga_update_view(request, vizsgaID):
    if is_EtrAdmin(request):
        obj = get_object_or_404(Vizsga, vizsgaID=vizsgaID)
        form = VizsgaForm(request.POST or None, instance=obj)
        if form.is_valid():
            form.save()
            return redirect("../../../vizsgak/")
        context = {
            'obj' : form
        }
        return render(request, "vizsga_creation.html", context)


def vizsga_lookup_view(request, vizsgaID):
    obj = get_object_or_404(Vizsga, vizsgaID=vizsgaID)

    context = {
        "obj": obj
    }
    return render(request, "vizsga_detail.html", context)


def vizsga_delete_view(request, vizsgaID):
    if is_EtrAdmin(request):
        obj = get_object_or_404(Vizsga, vizsgaID=vizsgaID)
        if request.method == "POST":
            obj.delete()
            return redirect("../../../vizsgak/")
        context = {
            "obj": obj
        }
        return render(request, "vizsga_delete.html", context)


def vizsga_list_view(request):
    queryset = Vizsga.objects.all()  #list of objects
    kodok = Vizsga.objects.all().values_list("vizsgaID", flat=True)
    felvettVizsgaAzonosito = list(Vizsgazik.objects.filter(hallgatoAzonosito=Hallgato.objects.get(azonosito=request.user)).values_list("vizsgaID", flat=True))
    felvettVizsgaTeljesitette = list(Vizsgazik.objects.filter(hallgatoAzonosito=Hallgato.objects.get(azonosito=request.user)).values_list("kapottjegy", flat=True))
    felvettVizsga = Vizsga.objects.filter(vizsgaID__in=felvettVizsgaAzonosito)
    
    felvettVizsga = zip(felvettVizsga, felvettVizsgaTeljesitette)
    
    felvett = Vizsgazik.objects.filter(hallgatoAzonosito=Hallgato.objects.get(azonosito=request.user))
    context = {
        "object_list": queryset,
        "felvettkodok": felvettVizsgaAzonosito,
    }
    return render(request, "vizsga_list.html", context)

def vizsga_add_view(request, vizsgaID):
    role = getRole(request.user)
    vizsga = Vizsga.objects.get(vizsgaID=vizsgaID)

    if role == "hallgato":
        hallgato = Hallgato.objects.get(azonosito=request.user)
        szamlalo = len(Vizsgazik.objects.filter(vizsgaID__kurzusKod=vizsga.kurzusKod, hallgatoAzonosito=hallgato))
        
        Vizsgazik.objects.create(vizsgaID=vizsga, hallgatoAzonosito=hallgato, kapottjegy=0, vizsgaalkalom=szamlalo+1)
    return redirect("../../../vizsgak/")

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

class VizsgaStatChartView(TemplateView):
    template_name = 'vizsgaStat.html'

    cursor = connection.cursor()
    cursor.execute(
        "SELECT round(avg(vizsgazik.kapottJegy), 2), vizsga.kurzusKod from vizsgazik, vizsga where vizsga.vizsgaID = vizsgazik.vizsgaID group by vizsga.kurzusKod;")
    r = dictfetchall(cursor)


    def get_context_data(self, **kwargs):
        listaAverage = []
        listaKurzusKod = []
        context = super().get_context_data(**kwargs)
        for x in self.r:
            listaAverage.append(x['ROUND(AVG(VIZSGAZIK.KAPOTTJEGY),2)'])
            listaKurzusKod.append(x['KURZUSKOD'])

        context["qs2"] = listaAverage
        context["qs1"] = listaKurzusKod

        return context