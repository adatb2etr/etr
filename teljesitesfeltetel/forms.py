from django import forms
from kurzus.forms import KurzusForm
from .models import Teljesitesfeltetel
from kepzes.forms import KepzesForm

class TeljesitesfeltetelForm(forms.ModelForm):

    kepzesId = KepzesForm()
    kurzusKod = KurzusForm()

    class Meta:
        model = Teljesitesfeltetel
        fields = [
            'kepzesId',
            'kurzusKod',
        ]

