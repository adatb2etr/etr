from django import forms
from user.forms import FelhasznaloForm
from .models import Befizetes


class BefizetesForm(forms.ModelForm):

    hallgatoAzonosito = FelhasznaloForm()
    befizetesosszeg = forms.IntegerField(widget=forms.TextInput(attrs={"placeholder": "Befizetés Összege"}))

    class Meta:
        model = Befizetes
        fields = [
            'hallgatoAzonosito',
            'befizetesosszeg',
        ]



class BefizetesFormUpdate(BefizetesForm):

    def __init__(self, *args, **kwargs):
        super(BefizetesFormUpdate, self).__init__(*args, **kwargs)
        self.fields['hallgatoAzonosito'].disabled = True