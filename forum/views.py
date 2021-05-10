from django.shortcuts import render, get_object_or_404
from user.models import EtrAdmin, Oktato, Hallgato
from user.validators.validators import is_EtrAdmin, is_Oktato, is_Hallgato
from django.shortcuts import redirect
from user.validators.queries import getids, getRole, getEtrAdminIds, getHallgatoIds, getOktatoIds
from .models import Oktato, OktatoUzenet, Hallgato, HallgatoUzenet
from itertools import chain
from .forms import HallgatoCommentForm, TemaFelvitelForm

# /me/forum
def sajat_forum_view(request):

    role = getRole(request.user)
    if role == "admin":
        user = EtrAdmin.objects.get(azonosito=request.user)
        try:
            queryset_o = OktatoUzenet.objects.order_by('-id', 'tema')
            queryset_h = HallgatoUzenet.objects.order_by('-id', 'tema')
            queryset = list(chain(queryset_h, queryset_o))
        except:
            queryset = []
        temaForm = TemaFelvitelForm(request.POST or None)
        if temaForm.is_valid():
            temaForm.save()
            temaForm = TemaFelvitelForm()
        form = HallgatoCommentForm(request.POST or None)
        if form.is_valid():
            form.userId = user
            form.save()
            form = HallgatoCommentForm()
        context = {
            "obj": user,
            "object_list": queryset,
            "form": form,
            "temaForm": temaForm,
            "role": role,
        }
        return render(request, "forum_view.html", context)
    elif role == "oktato":
        user = Oktato.objects.get(azonosito=request.user)
        queryset_o = OktatoUzenet.objects.order_by('-id', 'tema')
        queryset_h = HallgatoUzenet.objects.order_by('-id', 'tema')
        queryset = list(chain(queryset_h, queryset_o))
        form = HallgatoCommentForm(request.POST or None)
        if form.is_valid():
            form.userId = user
            form.save()
            form = HallgatoCommentForm()
        context = {
            "obj": user,
            "object_list": queryset,
            "form": form,
            "role": role,
        }
        return render(request, "forum_view.html", context)
    elif role == "hallgato":
        user = Hallgato.objects.get(azonosito=request.user)
        queryset_o = OktatoUzenet.objects.order_by('-id', 'tema')
        queryset_h = HallgatoUzenet.objects.order_by('-id', 'tema')
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
            "form": form,
            "role": role,
        }
        return render(request, "forum_view.html", context)
    else:
        return redirect("../teszt/")


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


def forum_lookup_view(request, message_id):
    try:
        obj = get_object_or_404(HallgatoUzenet, id=message_id)
    except:
        try:
            obj = get_object_or_404(OktatoUzenet, id=message_id)
        except:
            pass

    context = {
        "obj": obj
    }
    return render(request, "befizetes_detail.html", context)

def forum_delete_view(request, message_id):
    if is_EtrAdmin(request):
        try:
            obj = get_object_or_404(HallgatoUzenet, id=message_id)
        except:
            try:
                obj = get_object_or_404(OktatoUzenet, id=message_id)
            except:
                pass
        if request.method == "POST":
            obj.delete()
            return redirect("../../../forum/")
        context = {
            "obj": obj
        }
        return render(request, "befizetes_delete.html", context)