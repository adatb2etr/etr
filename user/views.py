import hashlib

from django.shortcuts import render, get_object_or_404, redirect
from user.forms import FelhasznaloForm, EtrAdminForm
from user.models import EtrAdmin, Oktato, Hallgato
from kurzus.models import Kurzus
from kurzustfelvesz.models import Kurzustfelvesz
from vizsga.models import Vizsga
from vizsgatfelvesz.models import VizsgatFelvesz
from user.forms import *
from user.validators.validators import is_EtrAdmin, is_Hallgato, is_Oktato
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from user.validators.queries import getids, getRole, getEtrAdminIds, getHallgatoIds, getOktatoIds
from django.http import HttpResponse
import sys


def felhasznalok_list_view(request):

    if is_EtrAdmin(request):
        queryset = Oktato.objects.all()  #list of objects
        queryset2 = Hallgato.objects.all()  #list of objects
        queryset = sorted(queryset, key=lambda Oktato: Oktato.vezeteknev)
        queryset2 = sorted(queryset2, key=lambda Hallgato: Hallgato.vezeteknev)
        context = {
            "object_list": queryset,
            "object_list2": queryset2,
        }
        return render(request, "felhasznalok/felhasznalok_list.html", context)
    else:
        return redirect("../../teszt/")

def felhasznalok_lookup_view(request, UserAzonosito):   # a UserAzonosító a  Models.py-ban megfelelő Modelből jön az urls.py megfelelő függvényén keresztül. path() -el kezdődik

    if is_EtrAdmin(request) or UserAzonosito == str(request.user):   # Ha a kérdező ADMIN VAGY SAJÁT akkor megnézi, hogy létezik-e oktató, ha nem akkor a hallgatót is, ha nem akkor pedig redirectel
            try:
                obj =Oktato.objects.get(azonosito=UserAzonosito)
            except:
                try:
                    obj = Hallgato.objects.get(azonosito=UserAzonosito)
                except:
                    try:
                        obj = EtrAdmin.objects.get(azonosito=UserAzonosito)
                    except:
                        return redirect("../../teszt/")
            context = {
                "obj": obj
            }
            return render(request, "felhasznalok/felhasznalok_detail.html", context)
    else:
        return redirect("../../teszt/")


def felhasznalok_update_view(request, UserAzonosito):

    if is_EtrAdmin(request) or UserAzonosito == str(request.user):

        try:
            obj = Oktato.objects.get(azonosito=UserAzonosito)
        except:
            try:
                obj = Hallgato.objects.get(azonosito=UserAzonosito)
            except:
                try:
                    obj = EtrAdmin.objects.get(azonosito=UserAzonosito)
                except:
                    return redirect("../../..teszt")



        form = FelhasznaloForm(request.POST or None, instance=obj)
        if form.is_valid():
            print("\n\n\nasdssasdadas\n\n\n")
            encryptedJelszo = (hashlib.sha256(form.data['jelszo'].encode())).hexdigest()

            obj.keresztnev =form.data['keresztnev']
            obj.vezeteknev=form.data['vezeteknev']
            obj.email=form.data['email']
            obj.jelszo=encryptedJelszo
            obj.telefonszam=form.data['telefonszam']
            obj.szulido=form.data['szulido']
            obj.szemelyiszam=form.data['szemelyiszam']
            obj.save()


            try:
                userJelszo = make_password(form.data['jelszo'])
                User.objects.filter(username=UserAzonosito).update(first_name=form.data['keresztnev'],
                                        last_name=form.data['vezeteknev']
                                        , email=form.data['email'], password=userJelszo)
            except:
                print("\n\nNem tudtam updateolni a Django felhasználót mert nem létezik!\n\n")
                sys.exc_info()

            return redirect("../../../felhasznalok/")
        context = {
            'form': form
        }
        return render(request, "register/dataChange.html", context)  #ez még csak temporális majd a frontendesek kicserélik LOL
    return redirect("../../..teszt")


def felhasznalok_delete_view(request, UserAzonosito):

    if is_EtrAdmin(request):
        try:
            obj = Oktato.objects.get(azonosito=UserAzonosito)
        except:
            try:
                obj = Hallgato.objects.get(azonosito=UserAzonosito)
            except:
                try:
                    obj = EtrAdmin.objects.get(azonosito=UserAzonosito)
                except:
                    return redirect("../../..teszt")

        if request.method == "POST":
            obj.delete()
            try:
                User.objects.get(username=UserAzonosito).delete()
            except:
                print("\n\nNem tudtam törölni a Django felhasználót mert nem létezik!\n\n")
                sys.exc_info()

            return redirect("../../../felhasznalok/")
        context = {
            "obj": obj
        }
        return render(request, "felhasznalok/felhasznalok_delete.html", context)
    return redirect("../../..teszt")

# /me
def sajat_detail_view(request):
    role = getRole(request.user)
    print(role)
    if role == "admin":
        user = EtrAdmin.objects.get(azonosito=request.user)
    elif role == "oktato":
        user = Oktato.objects.get(azonosito=request.user)
    elif role == "hallgato":
        user = Hallgato.objects.get(azonosito=request.user)
    else:
        return redirect("../teszt/")

    context = {
        "obj": user,
        "role" : role
    }
    return render(request, "felhasznalok/sajat_detail.html", context)


def sajat_kurzus_view(request):
    role = getRole(request.user)
    felvettKurzusok = None
    felvettKurzusokTeljesitette = None

    if role == "admin":
        user = EtrAdmin.objects.get(azonosito=request.user)
        kurzusok = Kurzus.objects.all()
    elif role == "oktato":
        user = Oktato.objects.get(azonosito=request.user)
        kurzusok = Kurzus.objects.filter(oktatoAzonosito=request.user)

    elif role == "hallgato":
        user = Hallgato.objects.get(azonosito=request.user)
        kurzusok = Kurzus.objects.filter(meghirdetett=1)
        felvettKurzusokAzonosito = list(Kurzustfelvesz.objects.filter(hallgatoAzonosito=user).values_list("kurzusKod", flat=True))
        felvettKurzusokTeljesitette = list(Kurzustfelvesz.objects.filter(hallgatoAzonosito=user).values_list("teljesitette", flat=True))
        felvettKurzusok = Kurzus.objects.filter(kurzuskod__in=felvettKurzusokAzonosito)
        
        felvettKurzusok = zip(felvettKurzusok, felvettKurzusokTeljesitette)

    else:
        return redirect("../teszt/")

    context = {
        "obj": user,
        "role" : role,
        "object_list": kurzusok,
        "felvettKurzusok": felvettKurzusok,
    }
    return render(request, "felhasznalok/sajat_kurzusok.html", context)

def sajat_vizsga_view(request):
    role = getRole(request.user)
    felvettVizsgak = None
    felvettVizsgakTeljesitette = None

    if role == "admin":
        user = EtrAdmin.objects.get(azonosito=request.user)
        vizsgak = Vizsga.objects.all()
    elif role == "oktato":
        user = Oktato.objects.get(azonosito=request.user)
        vizsgak = Vizsga.objects.filter(oktatoAzonosito=request.user)

    elif role == "hallgato":
        user = Hallgato.objects.get(azonosito=request.user)
        vizsgak = Vizsga.objects.all()
        felvettVizsgakAzonosito = list(VizsgatFelvesz.objects.filter(hallgatoAzonosito=user).values_list("vizsgaID", flat=True))
        felvettVizsgakTeljesitette = list(VizsgatFelvesz.objects.filter(hallgatoAzonosito=user).values_list("erdemjegy", flat=True))
        felvettVizsgak = Vizsga.objects.filter(vizsgaID__in=felvettVizsgakAzonosito)

        felvettVizsgak = zip(felvettVizsgak, felvettVizsgakTeljesitette)

    else:
        return redirect("../teszt/")

    context = {
        "obj": user,
        "role" : role,
        "object_list": vizsgak,
        "felvettVizsgak": felvettVizsgak,
    }
    return render(request, "felhasznalok/sajat_vizsgak.html", context)