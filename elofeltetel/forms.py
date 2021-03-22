from django import forms
from kurzus.forms import KurzusForm
from .models import Elofeltetel


class ElofeltetelForm(forms.ModelForm):

    kurzusKod = KurzusForm()
    elofeltetelKod = KurzusForm()

    class Meta:
        model = Elofeltetel
        fields = [
            'kurzusKod',
            'elofeltetelKod',
        ]