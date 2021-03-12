from django.shortcuts import render, get_object_or_404
from .forms import KurzusForm
from .models import Kurzus
from user.validators.validators import is_EtrAdmin
from django.shortcuts import redirect
from django.shortcuts import render



def kurzus_create_view(request):

    if is_EtrAdmin(request):
        if is_EtrAdmin(request) is True:
            form = KurzusForm(request.POST or None)
            if form.is_valid():
                form.save()
                form = KurzusForm()

            context = {
                'obj' : form
            }

            return render(request, 'kurzus_creation.html', context)


def kurzus_update_view(request, kurzus_kod):
    if is_EtrAdmin(request):
        obj = get_object_or_404(Kurzus, kurzuskod=kurzus_kod)
        form = KurzusForm(request.POST or None, instance=obj)
        if form.is_valid():
            form.save()
            return redirect("../../../kurzusok/")
        context = {
            'obj' : form
        }
        return render(request, "kurzus_creation.html", context)

def kurzus_lookup_view(request, kurzus_kod):
    obj = get_object_or_404(Kurzus, kurzuskod=kurzus_kod)

    context = {
        "obj": obj
    }
    return render(request, "kurzus_detail.html", context)

def kurzus_delete_view(request, kurzus_kod):
    if is_EtrAdmin(request):
        obj = get_object_or_404(Kurzus, kurzuskod=kurzus_kod)
        if request.method == "POST":
            obj.delete()
            return redirect("../../../kurzusok/")
        context = {
            "obj": obj
        }
        return render(request, "kurzus_delete.html", context)


def kurzus_list_view(request):
    queryset = Kurzus.objects.all()  #list of objects

    context = {
        "object_list": queryset
    }
    return render(request, "kurzus_list.html", context)

