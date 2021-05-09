from django import forms
from uzenofal.models import Uzenet

class UzenofalForm(forms.ModelForm):

    cim = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Uzenet címe"}))
    uzenet = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Uzenet tartalma"}))

    class Meta:
        model = Uzenet
        fields = [
            'cim',
            'uzenet',
        ]
