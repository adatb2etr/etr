from django.shortcuts import render, get_object_or_404
from .forms import KurzustFelveszForm
from .models import Kurzustfelvesz
from kurzus.models import Kurzus
from user.validators.validators import is_EtrAdmin
from django.shortcuts import redirect
from django.shortcuts import render
from elofeltetel.models import Elofeltetel

def get_teljesitett_elofeltetelek(kurzuskod, hallgatoAzonosito):
    elofeltetelek = Elofeltetel.objects.filter(kurzusKod=kurzuskod)
    teljesitettTantargyak = Kurzustfelvesz.objects.filter(hallgatoAzonosito=hallgatoAzonosito, teljesitette=1)

    elofeltetelekLista = list()
    teljesitettTantargyakLista = list()

    for x in elofeltetelek:
        elofeltetelekLista.append(x.elofeltetelKod.kurzuskod)

    for x in teljesitettTantargyak:
        teljesitettTantargyakLista.append(x.kurzusKod.kurzuskod)

    if all(elem in teljesitettTantargyakLista for elem in elofeltetelekLista) is True:
        return True
    else:
        return False


def meghirdetve(kurzuskod):
    try:
        tantargy = Kurzus.objects.get(kurzuskod=kurzuskod)
        if tantargy.oktatoAzonosito is None:
            return False
        else:
            return True
    except:
        print("\n\n\n dassaddsa \n\n\n")
        return False


def kurzustfelvesz_create_view(request):

    if is_EtrAdmin(request):
        if is_EtrAdmin(request) is True:
            form = KurzustFelveszForm(request.POST or None)
            if form.is_valid():

                felveszKkod = form.data['kurzusKod']
                hallgAzonosito = form.data['hallgatoAzonosito']


                if meghirdetve(felveszKkod) is True and get_teljesitett_elofeltetelek(felveszKkod, hallgAzonosito):

                    form.save()
                    form = KurzustFelveszForm()

            context = {
                'obj' : form
            }

            return render(request, 'kurzustfelvesz_creation.html', context)


def kurzustfelvesz_update_view(request, kurzustfelvesz_id):
    if is_EtrAdmin(request):
        obj = get_object_or_404(Kurzustfelvesz, id=kurzustfelvesz_id)
        form = KurzustFelveszForm(request.POST or None, instance=obj)
        if form.is_valid():
            form.save()
            return redirect("../../../kurzusokatfelvesz/")
        context = {
            'obj' : form
        }
        return render(request, "kurzustfelvesz_creation.html", context)

def kurzustfelvesz_lookup_view(request, kurzustfelvesz_id):
    obj = get_object_or_404(Kurzustfelvesz, id=kurzustfelvesz_id)

    context = {
        "obj": obj
    }
    return render(request, "kurzustfelvesz_detail.html", context)

def kurzustfelvesz_delete_view(request, kurzustfelvesz_id):
    if is_EtrAdmin(request):
        obj = get_object_or_404(Kurzustfelvesz, id=kurzustfelvesz_id)
        if request.method == "POST":
            obj.delete()
            return redirect("../../../kurzusokatfelvesz/")
        context = {
            "obj": obj
        }
        return render(request, "kurzustfelvesz_delete.html", context)


def kurzustfelvesz_list_view(request):
    queryset = Kurzustfelvesz.objects.all()  #list of objects

    context = {
        "object_list": queryset
    }
    return render(request, "kurzustfelvesz_list.html", context)

