from django import forms
from vizsga.forms import VizsgaForm
from user.forms import FelhasznaloForm
from .models import Vizsgazik

KAPOTTJEGYEK = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
)

VIZSGAALKALMAK = ((1, 1), (2, 2), (3, 3))

class VizsgazikForm(forms.ModelForm):

    vizsgaID = VizsgaForm()
    hallgatoAzonosito = FelhasznaloForm()
    kapottjegy = forms.TypedChoiceField(choices=KAPOTTJEGYEK, coerce=int)
    vizsgaalkalom = forms.TypedChoiceField(choices=VIZSGAALKALMAK, coerce=int)

    class Meta:
        model = Vizsgazik
        fields = [
            'vizsgaID',
            'hallgatoAzonosito',
            'vizsgaalkalom',
            'kapottjegy',
        ]
