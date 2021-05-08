from django.shortcuts import render, get_object_or_404
from .forms import BefizetesForm, BefizetesFormUpdate
from .models import Befizetes
from tartozas.models import Tartozas
from user.validators.validators import is_EtrAdmin
from django.shortcuts import redirect
from django.shortcuts import render



def befizetes_create_view(request):

    if is_EtrAdmin(request):
        if is_EtrAdmin(request) is True:
            form = BefizetesForm(request.POST or None)
            if form.is_valid():

                tartozasObj = Tartozas.objects.get(hallgatoAzonosito__azonosito=form.data['hallgatoAzonosito'])
                tartozasAzonosito = tartozasObj.hallgatoAzonosito
                ujtartozasosszeg = tartozasObj.tartozasosszeg - int(form.data['befizetesosszeg'])

                tartozasObj.delete()
                Tartozas.objects.create(tartozasosszeg=ujtartozasosszeg, hallgatoAzonosito=tartozasAzonosito)


                form.save()
                form = BefizetesForm()

            context = {
                'obj' : form
            }

            return render(request, 'befizetes_creation.html', context)


def befizetes_update_view(request, befizetesID):
    if is_EtrAdmin(request):
        obj = get_object_or_404(Befizetes, id=befizetesID)
        form = BefizetesFormUpdate(request.POST or None, instance=obj)
        if form.is_valid():
            obj.save()
            return redirect("../../../befizetesek/")
        context = {
            'obj' : form
        }
        return render(request, "befizetes_creation.html", context)

def befizetes_lookup_view(request, befizetesID):
    obj = get_object_or_404(Befizetes, id=befizetesID)

    context = {
        "obj": obj
    }
    return render(request, "befizetes_detail.html", context)

def befizetes_delete_view(request, befizetesID):
    if is_EtrAdmin(request):
        obj = get_object_or_404(Befizetes, id=befizetesID)
        if request.method == "POST":
            obj.delete()
            return redirect("../../../befizetesek/")
        context = {
            "obj": obj
        }
        return render(request, "befizetes_delete.html", context)


def befizetes_list_view(request):
    queryset = Befizetes.objects.all()  #list of objects

    context = {
        "object_list": queryset
    }
    return render(request, "befizetes_list.html", context)


