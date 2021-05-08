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
from .models import Info
from .forms import InfosheetForm

# Create your views here.
# /me/infosheet
def infosheet_view(request):
    print(request.user)
    role = getRole(request.user)
    if role == "admin":
        user = EtrAdmin.objects.get(azonosito=request.user)
        try:
            queryset = Info.objects.all()
        except Info.DoesNotExist:
            queryset = [Info("Hiba!", "Sajnos nincsenek még bejegyzések")]
        form = InfosheetForm(request.POST or None)
        if form.is_valid():
            form.save()
            form = InfosheetForm()              
        context = {
            "obj": user,
            "role" : role,
            "object_list": queryset,
            "form": form
        }
        return render(request, "infosheet_view.html", context)
    elif role == "oktato":
        user = Oktato.objects.get(azonosito=request.user)
        try:
            queryset = Info.objects.all()
        except Info.DoesNotExist:
            queryset = [Info("Hiba!", "Sajnos nincsenek még bejegyzések")]
        form = InfosheetForm(request.POST or None)
        if form.is_valid():
            form.save()
            form = InfosheetForm()              
        context = {
            "obj": user,
            "role" : role,
            "object_list": queryset,
            "form": form
        }
        return render(request, "infosheet_view.html", context)
    elif role == "hallgato":
        user = Hallgato.objects.get(azonosito=request.user)
        try:
            queryset = Info.objects.all()
        except Info.DoesNotExist:
            queryset = [Info("Hiba!", "Sajnos nincsenek még bejegyzések")]
        form = InfosheetForm(request.POST or None)
        if form.is_valid():
            form.save()
            form = InfosheetForm()              
        context = {
            "obj": user,
            "role" : role,
            "object_list": queryset,
            "form": form
        }
        return render(request, "infosheet_view.html", context)
    else:
        return redirect("../teszt/")

    context = {
        "obj": user,
        "role" : role
    }
    return render(request, "infosheet_view.html", context)