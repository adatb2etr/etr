from django.shortcuts import render, get_object_or_404
from .forms import ElofeltetelForm
from .models import Elofeltetel
from user.validators.validators import is_EtrAdmin
from django.shortcuts import redirect
from django.shortcuts import render



def elofeltetel_create_view(request):

    if is_EtrAdmin(request):
        if is_EtrAdmin(request) is True:
            form = ElofeltetelForm(request.POST or None)

            if form.is_valid():
                tantargyKod = form.data['kurzusKod']
                elofeltetelKod = form.data['elofeltetelKod']

                if tantargyKod != elofeltetelKod:
                    form.save()
                    form = ElofeltetelForm()

            context = {
                'obj' : form
            }

            return render(request, 'elofeltetel_creation.html', context)


def elofeltetel_update_view(request, elofeltetel_id):
    if is_EtrAdmin(request):
        obj = get_object_or_404(Elofeltetel, id=elofeltetel_id)
        form = ElofeltetelForm(request.POST or None, instance=obj)
        if form.is_valid():
            form.save()
            return redirect("../../../elofeltetelek/")
        context = {
            'obj' : form
        }
        return render(request, "elofeltetel_creation.html", context)

def elofeltetel_lookup_view(request, elofeltetel_id):
    obj = get_object_or_404(Elofeltetel, id=elofeltetel_id)

    context = {
        "obj": obj
    }
    return render(request, "elofeltetel_detail.html", context)

def elofeltetel_delete_view(request, elofeltetel_id):
    if is_EtrAdmin(request):
        obj = get_object_or_404(Elofeltetel, id=elofeltetel_id)
        if request.method == "POST":
            obj.delete()
            return redirect("../../../elofeltetelek/")
        context = {
            "obj": obj
        }
        return render(request, "elofeltetel_delete.html", context)


def elofeltetel_list_view(request):
    queryset = Elofeltetel.objects.all()  #list of objects

    context = {
        "object_list": queryset
    }
    return render(request, "elofeltetel_list.html", context)

