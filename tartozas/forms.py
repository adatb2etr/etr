from django import forms
from user.forms import FelhasznaloForm
from .models import Tartozas


class TartozasForm(forms.ModelForm):

    hallgatoAzonosito = FelhasznaloForm()
    befizetesOsszege = forms.IntegerField(widget=forms.TextInput(attrs={"placeholder": "Tartozas Összege"}))

    class Meta:
        model = Tartozas
        fields = [
            'hallgatoAzonosito',
            'befizetesOsszege',
        ]

class TartozasFormUpdate(TartozasForm):

    def __init__(self, *args, **kwargs):
        super(TartozasFormUpdate, self).__init__(*args, **kwargs)
        self.fields['hallgatoAzonosito'].disabled = True