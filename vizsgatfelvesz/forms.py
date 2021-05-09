from django import forms
from user.forms import FelhasznaloForm
from .models import Vizsgatfelvesz


class VizsgatFelveszForm(forms.ModelForm):

    hallgatoAzonosito = FelhasznaloForm()
    vizsgaID = forms.IntegerField
    evszam = forms.IntegerField

    class Meta:
        model = Vizsgatfelvesz
        fields = [
            'hallgatoAzonosito',
            'vizsgaID',
            'evszam',
        ]