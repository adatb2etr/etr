from django.shortcuts import render, get_object_or_404
from .forms import KepzesForm, KepzesFormUpdate
from .models import Kepzes
from user.validators.validators import is_EtrAdmin
from django.shortcuts import redirect
from django.shortcuts import render



def kepzes_create_view(request):

    if is_EtrAdmin(request):
        if is_EtrAdmin(request) is True:
            form = KepzesForm(request.POST or None)
            if form.is_valid():
                form.save()
                form = KepzesForm()

            context = {
                'obj' : form
            }

            return render(request, 'kepzes_creation.html', context)


def kepzes_update_view(request, kepzesid):
    if is_EtrAdmin(request):
        obj = get_object_or_404(Kepzes, kepzesid=kepzesid)
        form = KepzesFormUpdate(request.POST or None, instance=obj)
        if form.is_valid():
            kepzesID = obj.kepzesid

            obj.delete()
            Kepzes.objects.create(kepzesid=kepzesID, nev=form.data['nev'])

            return redirect("../../../kepzesek/")
        context = {
            'obj' : form
        }
        return render(request, "kepzes_creation.html", context)

def kepzes_lookup_view(request, kepzesid):
    obj = get_object_or_404(Kepzes, kepzesid=kepzesid)

    context = {
        "obj": obj
    }
    return render(request, "kepzes_detail.html", context)

def kepzes_delete_view(request, kepzesid):
    if is_EtrAdmin(request):
        obj = get_object_or_404(Kepzes, kepzesid=kepzesid)
        if request.method == "POST":
            obj.delete()
            return redirect("../../../kepzesek/")
        context = {
            "obj": obj
        }
        return render(request, "kepzes_delete.html", context)


def kepzes_list_view(request):
    queryset = Kepzes.objects.all()  #list of objects

    context = {
        "object_list": queryset
    }
    return render(request, "kepzes_list.html", context)


