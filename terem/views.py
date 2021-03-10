from django.shortcuts import render, get_object_or_404
from terem.forms import TeremForm, TeremFormUpdate
from terem.models import Terem
from user.validators.validators import is_EtrAdmin
from django.shortcuts import redirect
from django.shortcuts import render



def terem_create_view(request):

    if is_EtrAdmin(request):
        if is_EtrAdmin(request) is True:
            form = TeremForm(request.POST or None)
            if form.is_valid():
                form.save()
                form = TeremForm()

            context = {
                'obj' : form
            }

            return render(request, 'terem_creation.html', context)


def terem_update_view(request, terem_cim):
    if is_EtrAdmin(request):
        obj = get_object_or_404(Terem, cim=terem_cim)
        form = TeremFormUpdate(request.POST or None, instance=obj)
        if form.is_valid():
            form.save()
            return redirect("../../../termek/")
        context = {
            'obj' : form
        }
        return render(request, "terem_creation.html", context)

def terem_lookup_view(request, terem_cim):
    obj = get_object_or_404(Terem, cim=terem_cim)

    context = {
        "obj": obj
    }
    return render(request, "terem_detail.html", context)

def terem_delete_view(request, terem_cim):
    if is_EtrAdmin(request):
        obj = get_object_or_404(Terem, cim=terem_cim)
        if request.method == "POST":
            obj.delete()
            return redirect("../../../termek/")
        context = {
            "obj": obj
        }
        return render(request, "terem_delete.html", context)


def terem_list_view(request):
    queryset = Terem.objects.all()  #list of objects
    context = {
        "object_list": queryset
    }
    return render(request, "terem_list.html", context)

