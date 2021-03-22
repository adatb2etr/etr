from django import forms
from kurzus.forms import KurzusForm
from user.forms import FelhasznaloForm
from .models import Kurzustfelvesz


class KurzustFelveszForm(forms.ModelForm):

    hallgatoAzonosito = FelhasznaloForm()
    kurzusKod = KurzusForm()

    class Meta:
        model = Kurzustfelvesz
        fields = [
            'hallgatoAzonosito',
            'kurzusKod',
        ]