import hashlib

from django.shortcuts import render, get_object_or_404, redirect
from user.forms import FelhasznaloForm, EtrAdminForm
from user.models import EtrAdmin, Oktato, Hallgato
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
            print(f"\n\n\nsfsdafsadsadds\n\n\n")
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
            encryptedJelszo = (hashlib.sha256(form.data['jelszo'].encode())).hexdigest()

            Oktato.objects.filter(azonosito=UserAzonosito).update(keresztnev=form.data['keresztnev'], vezeteknev=form.data['vezeteknev']
                                  ,email=form.data['email'], jelszo=encryptedJelszo, telefonszam=form.data['telefonszam'],
                                  szulido=form.data['szulido'],
                                  szemelyiszam=form.data['szemelyiszam'])

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
        return render(request, "register/registerFelhasznalo.html", context)  #ez még csak temporális majd a frontendesek kicserélik LOL
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


def sajat_detail_view(request):

    if is_EtrAdmin(request):
        user = EtrAdmin.objects.get(azonosito=request.user)
    elif is_Oktato(request):
        user = Oktato.objects.get(azonosito=request.user)
    elif is_Hallgato(request):
        user = Hallgato.objects.get(azonosito=request.user)
    else:
        return redirect("../teszt/")

    context = {
        "obj": user
    }
    return render(request, "felhasznalok/sajat_detail.html", context)