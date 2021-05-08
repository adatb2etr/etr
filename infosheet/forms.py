from infosheet.models import Info
from django import forms

class InfosheetForm(forms.ModelForm):

    cim = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Info címe"}))
    uzenet = forms.IntegerField(widget=forms.TextInput(attrs={"placeholder": "Info üzenete"}))

    class Meta:
        model = Info
        fields = [
            'cim',
            'uzenet',
        ]
