from django.shortcuts import render, get_object_or_404
from .forms import IdopontForm
from .models import Idopont
from user.validators.validators import is_EtrAdmin
from django.shortcuts import redirect
from django.shortcuts import render



def idopont_create_view(request):

    if is_EtrAdmin(request):
        if is_EtrAdmin(request) is True:
            form = IdopontForm(request.POST or None)
            if form.is_valid():
                form.save()
                form = IdopontForm()

            context = {
                'obj' : form
            }

            return render(request, 'idopont_creation.html', context)


def idopont_update_view(request, idopont_id):
    if is_EtrAdmin(request):
        obj = get_object_or_404(Idopont, id=idopont_id)
        form = IdopontForm(request.POST or None, instance=obj)
        if form.is_valid():
            form.save()
            return redirect("../../../idopontok/")
        context = {
            'obj' : form
        }
        return render(request, "idopont_creation.html", context)

def idopont_lookup_view(request, idopont_id):
    print(f"\n\n\n{idopont_id}\n\n\n\n")
    obj = get_object_or_404(Idopont, id=idopont_id)

    context = {
        "obj": obj
    }
    return render(request, "idopont_detail.html", context)

def idopont_delete_view(request, idopont_id):
    if is_EtrAdmin(request):
        obj = get_object_or_404(Idopont, id=idopont_id)
        if request.method == "POST":
            obj.delete()
            return redirect("../../../idopontok/")
        context = {
            "obj": obj
        }
        return render(request, "idopont_delete.html", context)


def idopont_list_view(request):
    queryset = Idopont.objects.all()  #list of objects

    context = {
        "object_list": queryset
    }
    return render(request, "idopont_list.html", context)

