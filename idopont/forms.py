from django import forms

from .models import Idopont
from kurzus.forms import KurzusForm


class IdopontForm(forms.ModelForm):

    kezdete = forms.DateTimeField()
    vege = forms.DateTimeField()
    kurzusKod = KurzusForm()

    class Meta:
        model = Idopont
        fields = ['kezdete',
                  'vege',
                  'kurzusKod',]
