from django.shortcuts import render, get_object_or_404
from .forms import TartozasForm, TartozasFormUpdate
from .models import Tartozas
from user.validators.validators import is_EtrAdmin
from django.shortcuts import redirect
from django.shortcuts import render



def tartozas_create_view(request):
    if is_EtrAdmin(request):
        if is_EtrAdmin(request) is True:
            form = TartozasForm(request.POST or None)
            if form.is_valid():
                form.save()
                form = TartozasForm()

            context = {
                'obj' : form
            }

            return render(request, 'tartozas_creation.html', context)


def tartozas_update_view(request, hallgatoAzonosito):
    if is_EtrAdmin(request):
        obj = get_object_or_404(Tartozas, hallgatoAzonosito=hallgatoAzonosito)
        form = TartozasFormUpdate(request.POST or None, instance=obj)
        if form.is_valid():
            hallgatoID = obj.hallgatoAzonosito
            tartozasOsszege = int(obj.tartozasosszeg)

            obj.delete()
            Tartozas.objects.create(hallgatoAzonosito=hallgatoID, tartozasosszeg=tartozasOsszege)


            return redirect("../../../tartozasok/")
        context = {
            'obj' : form
        }
        return render(request, "tartozas_creation.html", context)

def tartozas_lookup_view(request, hallgatoAzonosito):
    obj = get_object_or_404(Tartozas, hallgatoAzonosito=hallgatoAzonosito)

    context = {
        "obj": obj
    }
    return render(request, "tartozas_detail.html", context)

def tartozas_delete_view(request, hallgatoAzonosito):
    if is_EtrAdmin(request):
        obj = get_object_or_404(Tartozas, hallgatoAzonosito=hallgatoAzonosito)
        if request.method == "POST":
            obj.delete()
            return redirect("../../../tartozasok/")
        context = {
            "obj": obj
        }
        return render(request, "tartozas_delete.html", context)


def tartozas_list_view(request):
    queryset = Tartozas.objects.all()  #list of objects
    form = TartozasForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = TartozasForm()
    context = {
        "object_list": queryset,
        "form": form
    }
    return render(request, "tartozas_list.html", context)


