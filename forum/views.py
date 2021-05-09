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
from .models import Oktato, OktatoUzenet, Hallgato, HallgatoUzenet
from itertools import chain
from .forms import HallgatoCommentForm

# /me/forum
def sajat_forum_view(request):
    role = getRole(request.user)
    if role == "admin":
        user = EtrAdmin.objects.get(azonosito=request.user)
        try:
            queryset_o = OktatoUzenet.objects.order_by('-id')
            queryset_h = HallgatoUzenet.objects.order_by('-id')
            queryset = list(chain(queryset_h, queryset_o))
        except:
            queryset = []
        form = HallgatoCommentForm(request.POST or None)
        if form.is_valid():
            form.userId = user
            form.save()
            form = HallgatoCommentForm()
        context = {
            "obj": user,
            "object_list": queryset,
            "form": form
        }
        return render(request, "forum_view.html", context)
    elif role == "oktato":
        user = Oktato.objects.get(azonosito=request.user)
        queryset_o = OktatoUzenet.objects.order_by('-id')
        queryset_h = HallgatoUzenet.objects.order_by('-id')
        queryset = list(chain(queryset_h, queryset_o))
        form = HallgatoCommentForm(request.POST or None)
        if form.is_valid():
            form.userId = user
            form.save()
            form = HallgatoCommentForm()
        context = {
            "obj": user,
            "object_list": queryset,
            "form": form
        }
        return render(request, "forum_view.html", context)
    elif role == "hallgato":
        user = Hallgato.objects.get(azonosito=request.user)
        queryset_o = OktatoUzenet.objects.order_by('-id')
        queryset_h = HallgatoUzenet.objects.order_by('-id')
        queryset = list(chain(queryset_h, queryset_o))
        form = HallgatoCommentForm(request.POST or None)
        if form.is_valid():
            form = form.save(commit=False)
            form.userId = user
            form.save()
            form = HallgatoCommentForm()
        context = {
            "obj": user,
            "object_list": queryset,
            "form": form
        }
        return render(request, "forum_view.html", context)
    else:
        return redirect("../teszt/")

    context = {
        "obj": user,
        "role" : role
    }
    return render(request, "forum_view.html", context)

    # /me/forum/edit
def forum_edit_view(request):
    print(request.user)
    role = getRole(request.user)
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
    return render(request, "forum_edit_view.html", context)

    # /me/forum/delete
def forum_delete_view(request):
    print(request.user)
    role = getRole(request.user)
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
    return render(request, "forum_delete_view.html", context)