from django.shortcuts import render, get_object_or_404
from .forms import TeljesitesfeltetelForm
from .models import Teljesitesfeltetel
from user.validators.validators import is_EtrAdmin
from django.shortcuts import redirect
from django.shortcuts import render


def teljesitesfeltetel_create_view(request):

    if is_EtrAdmin(request):
        if is_EtrAdmin(request) is True:
            form = TeljesitesfeltetelForm(request.POST or None)
            if form.is_valid():
                form.save()
                form = TeljesitesfeltetelForm()

            context = {
                'obj' : form
            }

            return render(request, 'teljesitesfeltetel_creation.html', context)


def teljesitesfeltetel_update_view(request, teljesitesfeltetelID):
    if is_EtrAdmin(request):
        obj = get_object_or_404(Teljesitesfeltetel, id=teljesitesfeltetelID)
        form = TeljesitesfeltetelForm(request.POST or None, instance=obj)
        if form.is_valid():
            form.save()
            return redirect("../../../teljesitesfeltetelek/")
        context = {
            'obj' : form
        }
        return render(request, "teljesitesfeltetel_creation.html", context)


def teljesitesfeltetel_lookup_view(request, teljesitesfeltetelID):
    obj = get_object_or_404(Teljesitesfeltetel, id=teljesitesfeltetelID)

    context = {
        "obj": obj
    }
    return render(request, "teljesitesfeltetel_detail.html", context)


def teljesitesfeltetel_delete_view(request, teljesitesfeltetelID):
    if is_EtrAdmin(request):
        obj = get_object_or_404(Teljesitesfeltetel, id=teljesitesfeltetelID)
        if request.method == "POST":
            obj.delete()
            return redirect("../../../teljesitesfeltetelek/")
        context = {
            "obj": obj
        }
        return render(request, "teljesitesfeltetel_delete.html", context)


def teljesitesfeltetel_list_view(request):
    queryset = Teljesitesfeltetel.objects.all()  #list of objects
    context = {
        "object_list": queryset
    }
    return render(request, "teljesitesfeltetel_list.html", context)

