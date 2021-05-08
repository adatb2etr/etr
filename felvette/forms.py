from django import forms
from user.forms import FelhasznaloForm
from .models import Felvette
from kepzes.forms import KepzesForm

class FelvetteForm(forms.ModelForm):

    hallgatoAzonosito = FelhasznaloForm()
    kepzesId = KepzesForm()

    class Meta:
        model = Felvette
        fields = [
            'hallgatoAzonosito',
            'kepzesId',
        ]

