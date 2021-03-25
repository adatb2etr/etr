from django.shortcuts import render, get_object_or_404
from .forms import VizsgazikForm
from .models import Vizsgazik
from vizsga.models import Vizsga
from user.validators.validators import is_EtrAdmin
from django.shortcuts import redirect
from django.shortcuts import render



def vizsgazik_create_view(request):

    if is_EtrAdmin(request):
        if is_EtrAdmin(request) is True:
            form = VizsgazikForm(request.POST or None)
            if form.is_valid():
                form.save()
                form = VizsgazikForm()

            context = {
                'obj' : form
            }

            return render(request, 'vizsgazik_creation.html', context)


def vizsgazik_update_view(request, vizsgazikID):
    if is_EtrAdmin(request):
        obj = get_object_or_404(Vizsgazik, id=vizsgazikID)
        form = VizsgazikForm(request.POST or None, instance=obj)
        if form.is_valid():
            form.save()
            return redirect("../../../vizsgazik/")
        context = {
            'obj' : form
        }
        return render(request, "vizsgazik_creation.html", context)


def vizsgazik_lookup_view(request, vizsgazikID):
    obj = get_object_or_404(Vizsgazik, id=vizsgazikID)

    context = {
        "obj": obj
    }
    return render(request, "vizsgazik_detail.html", context)


def vizsgazik_delete_view(request, vizsgazikID):
    if is_EtrAdmin(request):
        obj = get_object_or_404(Vizsgazik, id=vizsgazikID)
        if request.method == "POST":
            obj.delete()
            return redirect("../../../vizsgazik/")
        context = {
            "obj": obj
        }
        return render(request, "vizsgazik_delete.html", context)


def vizsgazik_list_view(request):
    queryset = Vizsgazik.objects.all()  #list of objects
    context = {
        "object_list": queryset
    }
    return render(request, "vizsgazik_list.html", context)

