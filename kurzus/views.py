from django.shortcuts import render, get_object_or_404
from .forms import KurzusForm
from .models import Kurzus
from kurzustfelvesz.models import Kurzustfelvesz
from user.validators.validators import is_EtrAdmin
from user.models import Hallgato
from django.shortcuts import redirect
from django.shortcuts import render
from user.validators.queries import getids, getRole, getEtrAdminIds, getHallgatoIds, getOktatoIds

def kurzus_create_view(request):
    role = getRole(request.user)
    if is_EtrAdmin(request) or role=="oktato":
        print("admin")
        form = KurzusForm(request.POST or None)
        if form.is_valid():
            form.save()
            form = KurzusForm()

        context = {
            'obj' : form
        }

        return render(request, 'kurzus_creation.html', context)


def kurzus_update_view(request, kurzus_kod):
    role = getRole(request.user)
    if is_EtrAdmin(request) or role=="oktato":
        obj = get_object_or_404(Kurzus, kurzuskod=kurzus_kod)
        form = KurzusForm(request.POST or None, instance=obj)
        if form.is_valid():
            form.save()
            return redirect("../../../kurzusok/")
        context = {
            'obj' : form
        }
        return render(request, "kurzus_creation.html", context)

def kurzus_lookup_view(request, kurzus_kod):
    user = request.user
    obj = get_object_or_404(Kurzus, kurzuskod=kurzus_kod)
    role = getRole(request.user)
    context = {
        "obj": obj,
        "role": role
    }
    return render(request, "kurzus_detail.html", context)

def kurzus_delete_view(request, kurzus_kod):
    if is_EtrAdmin(request):
        obj = get_object_or_404(Kurzus, kurzuskod=kurzus_kod)
        if request.method == "POST":
            obj.delete()
            return redirect("../../../kurzusok/")
        context = {
            "obj": obj
        }
        return render(request, "kurzus_delete.html", context)

def kurzus_list_view(request):
    role = getRole(request.user)
    queryset = Kurzus.objects.all()  #list of objects
    kodok = Kurzus.objects.all().values_list("kurzuskod", flat=True)
    felvettKurzusokAzonosito = list(Kurzustfelvesz.objects.filter(hallgatoAzonosito=Hallgato.objects.get(azonosito=request.user)).values_list("kurzusKod", flat=True))
    felvettKurzusokTeljesitette = list(Kurzustfelvesz.objects.filter(hallgatoAzonosito=Hallgato.objects.get(azonosito=request.user)).values_list("teljesitette", flat=True))
    felvettKurzusok = Kurzus.objects.filter(kurzuskod__in=felvettKurzusokAzonosito)
    
    felvettKurzusok = zip(felvettKurzusok, felvettKurzusokTeljesitette)
    
    felvett = Kurzustfelvesz.objects.filter(hallgatoAzonosito=Hallgato.objects.get(azonosito=request.user))

    context = {
        "object_list": queryset,
        "role": role,
        "azonosito": request.user,
        "felvettkodok": felvettKurzusokAzonosito,
    }
    return render(request, "kurzus_list.html", context)

def kurzus_add_view(request, kurzus_kod):
    queryset = Kurzus.objects.all()  #list of objects
    role = getRole(request.user)
    user = request.user
    print(user)
    if role == "hallgato":
        obj = get_object_or_404(Kurzus, kurzuskod=kurzus_kod)
        Kurzustfelvesz(hallgatoAzonosito=Hallgato.objects.get(azonosito=user), kurzusKod=obj, teljesitette=0, evszam=2021).save()
        return redirect("../../../kurzusok/")
    context = {
        "object_list": queryset
    }
    return redirect("../../../kurzusok/")

def kurzus_disable_view(request, kurzus_kod):
    if is_Oktato(request):
        obj = get_object_or_404(Kurzus, kurzuskod=kurzus_kod)
        if request.method == "POST":
            obj.update(meghirdetett=0)
            return redirect("../../../kurzusok/")
        context = {
            "obj": obj
        }
        return redirect("../../../kurzusok/")

def kurzusKiosztas():
    osszesKurzus = list(Kurzus.objects.values_list('kurzuskod', flat=True).filter(meghirdetett=0, oktatoAzonosito=None))
    osszesOktato = list(Oktato.objects.all())


    while True:
        try:
            kurzustKiosztani = random.choice(osszesKurzus)
            kurzushozOktato = random.choice(osszesOktato)
            osszesKurzus.remove(kurzustKiosztani)
            kurzus = Kurzus.objects.get(kurzuskod=kurzustKiosztani)
            kurzus.oktatoAzonosito = kurzushozOktato
            kurzus.save()
        except:
            break