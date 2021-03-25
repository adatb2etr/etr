from django.shortcuts import render, get_object_or_404
from .forms import VizsgaForm
from .models import Vizsga
from user.validators.validators import is_EtrAdmin
from django.shortcuts import redirect
from django.shortcuts import render



def vizsga_create_view(request):

    if is_EtrAdmin(request):
        if is_EtrAdmin(request) is True:
            form = VizsgaForm(request.POST or None)
            if form.is_valid():
                form.save()
                form = VizsgaForm()

            context = {
                'obj' : form
            }

            return render(request, 'vizsga_creation.html', context)


def vizsga_update_view(request, vizsgaID):
    if is_EtrAdmin(request):
        obj = get_object_or_404(Vizsga, vizsgaID=vizsgaID)
        form = VizsgaForm(request.POST or None, instance=obj)
        if form.is_valid():
            form.save()
            return redirect("../../../vizsgak/")
        context = {
            'obj' : form
        }
        return render(request, "vizsga_creation.html", context)


def vizsga_lookup_view(request, vizsgaID):
    obj = get_object_or_404(Vizsga, vizsgaID=vizsgaID)

    context = {
        "obj": obj
    }
    return render(request, "vizsga_detail.html", context)


def vizsga_delete_view(request, vizsgaID):
    if is_EtrAdmin(request):
        obj = get_object_or_404(Vizsga, vizsgaID=vizsgaID)
        if request.method == "POST":
            obj.delete()
            return redirect("../../../vizsgak/")
        context = {
            "obj": obj
        }
        return render(request, "vizsga_delete.html", context)


def vizsga_list_view(request):
    queryset = Vizsga.objects.all()  #list of objects
    context = {
        "object_list": queryset
    }
    return render(request, "vizsga_list.html", context)

