from django.shortcuts import render, get_object_or_404
from .forms import OsztondijForm, OsztondijFormUpdate
from .models import Osztondij
from user.validators.validators import is_EtrAdmin
from django.shortcuts import redirect
from django.shortcuts import render



def osztondij_create_view(request):

    if is_EtrAdmin(request):
        if is_EtrAdmin(request) is True:
            form = OsztondijForm(request.POST or None)
            if form.is_valid():
                form.save()
                form = OsztondijForm()

            context = {
                'obj' : form
            }

            return render(request, 'osztondij_creation.html', context)


def osztondij_update_view(request, hallgatoAzonositoOsztondij):
    if is_EtrAdmin(request):
        obj = get_object_or_404(Osztondij, hallgatoAzonosito=hallgatoAzonositoOsztondij)
        form = OsztondijFormUpdate(request.POST or None, instance=obj)
        if form.is_valid():
            hallgatoID = obj.hallgatoAzonosito

            obj.delete()
            Osztondij.objects.create(hallgatoAzonosito=hallgatoID, osztondijosszeg=int(form.data['osztondijOsszege']))

            return redirect("../../../osztondijjak/")
        context = {
            'obj' : form
        }
        return render(request, "osztondij_creation.html", context)

def osztondij_lookup_view(request, hallgatoAzonositoOsztondij):
    obj = get_object_or_404(Osztondij, hallgatoAzonosito=hallgatoAzonositoOsztondij)

    context = {
        "obj": obj
    }
    return render(request, "osztondij_detail.html", context)

def osztondij_delete_view(request, hallgatoAzonositoOsztondij):
    if is_EtrAdmin(request):
        obj = get_object_or_404(Osztondij, hallgatoAzonosito=hallgatoAzonositoOsztondij)
        if request.method == "POST":
            obj.delete()
            return redirect("../../../osztondijjak/")
        context = {
            "obj": obj
        }
        return render(request, "osztondij_delete.html", context)


def osztondij_list_view(request):
    queryset = Osztondij.objects.all()  #list of objects

    context = {
        "object_list": queryset
    }
    return render(request, "osztondij_list.html", context)


