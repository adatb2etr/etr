from django import forms
from kurzus.forms import KurzusForm
from .models import Vizsga

class VizsgaForm(forms.ModelForm):

    vizsgaID = Vizsga.vizsgaID
    kurzusKod = KurzusForm()
    idopont = forms.DateTimeField(input_formats=['%Y-%m-%d %H:%M:%S'])
    ferohely = forms.IntegerField(widget=forms.TextInput(attrs={"placeholder": "Maximális létszám"}))

    class Meta:
        model = Vizsga
        fields = [
            'vizsgaID',
            'kurzusKod',
            'idopont',
            'ferohely',
        ]