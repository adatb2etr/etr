from django.shortcuts import render, get_object_or_404
from .forms import FelvetteForm
from .models import Felvette
from user.validators.validators import is_EtrAdmin
from django.shortcuts import redirect
from django.shortcuts import render



def felvette_create_view(request):

    if is_EtrAdmin(request):
        if is_EtrAdmin(request) is True:
            form = FelvetteForm(request.POST or None)
            if form.is_valid():
                form.save()
                form = FelvetteForm()

            context = {
                'obj' : form
            }

            return render(request, 'felvette_creation.html', context)


def felvette_update_view(request, felvetteID):
    if is_EtrAdmin(request):
        obj = get_object_or_404(Felvette, id=felvetteID)
        form = FelvetteForm(request.POST or None, instance=obj)
        if form.is_valid():
            form.save()
            return redirect("../../../felvette/")
        context = {
            'obj' : form
        }
        return render(request, "felvette_creation.html", context)


def felvette_lookup_view(request, felvetteID):
    obj = get_object_or_404(Felvette, id=felvetteID)

    context = {
        "obj": obj
    }
    return render(request, "felvette_detail.html", context)


def felvette_delete_view(request, felvetteID):
    if is_EtrAdmin(request):
        obj = get_object_or_404(Felvette, id=felvetteID)
        if request.method == "POST":
            obj.delete()
            return redirect("../../../felvette/")
        context = {
            "obj": obj
        }
        return render(request, "felvette_delete.html", context)


def felvette_list_view(request):
    queryset = Felvette.objects.all()  #list of objects
    context = {
        "object_list": queryset
    }
    return render(request, "felvette_list.html", context)

