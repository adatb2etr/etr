from django.shortcuts import render
from user.forms import EtrAdminForm, FelhasznaloForm, FelhasznaloLoginForm
from user.models import EtrAdmin, Oktato, Hallgato
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import hashlib
from django.contrib.auth.hashers import make_password
from user.validators.validators import is_EtrAdmin, is_Oktato, is_Hallgato
from user.validators.queries import getids
from django.shortcuts import redirect
from tartozas.admin import Tartozas
from osztondij.models import Osztondij
import random, string
from django.contrib.auth.forms import UserCreationForm
from user.validators.queries import getids, getRole, getEtrAdminIds, getHallgatoIds, getOktatoIds
from .models import Uzenet
from .forms import UzenofalForm

# Create your views here.
# /me/uzenofal
def uzenofal_view(request):
    role = getRole(request.user)
    print(role)
    if role == "admin":
        user = EtrAdmin.objects.get(azonosito=request.user)
        try:
            queryset = Uzenet.objects.all()
        except Uzenet.DoesNotExist:
            queryset = [Uzenet("Hiba!", "Sajnos nincsenek még bejegyzések")]
        form = UzenofalForm(request.POST or None)
        if form.is_valid():
            form.save()
            form = UzenofalForm()        
        context = {
            "obj": user,
            "role" : role,
            "object_list": queryset,
            "form": form
        }
        return render(request, "uzenofal_view.html", context)
    elif role == "oktato":
        user = Oktato.objects.get(azonosito=request.user)        
        try:
            queryset = Uzenet.objects.all()
        except Uzenet.DoesNotExist:
            queryset = [Uzenet("Hiba!", "Sajnos nincsenek még bejegyzések")]
        form = UzenofalForm(request.POST or None)
        if form.is_valid():
            form.save()
            form = UzenofalForm()
        context = {
            "obj": user,
            "role" : role,
            "object_list": queryset,
            "form": form
        }
        return render(request, "uzenofal_view.html", context)
    elif role == "hallgato":
        user = Hallgato.objects.get(azonosito=request.user)
        try:
            queryset = Uzenet.objects.all()
        except Uzenet.DoesNotExist:
            queryset = [Uzenet("Hiba!", "Sajnos nincsenek még bejegyzések")]
        form = UzenofalForm(request.POST or None)
        if form.is_valid():
            form.save()
            form = UzenofalForm()
        context = {
            "obj": user,
            "role" : role,
            "object_list": queryset,
            "form": form
        }
        return render(request, "uzenofal_view.html", context)
    else:
        return redirect("../teszt/")

    context = {
        "obj": user,
        "role" : role
    }
    return render(request, "uzenofal_view.html", context)

def uzenofal_create_view(request):
    if is_Oktato(request):
        if is_Oktato(request) is True:
            form = UzenofalForm(request.POST or None)
            if form.is_valid():
                form.save()
                form = UzenofalForm()

            context = {
                'form' : form
            }

            return render(request, 'uzenofal_creation.html', context)


def uzenofal_delete_view(request, id):
    if is_Oktato(request):
        obj = get_object_or_404(Uzenet, id=id)
        if request.method == "POST":
            obj.delete()
            return redirect("../../../uzenofal/")
        context = {
            "obj": obj
        }
        return render(request, "uzenofal_delete.html", context)