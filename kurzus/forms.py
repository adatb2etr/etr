from django import forms
from user.forms import FelhasznaloForm
from terem.forms import TeremForm
from .models import Kurzus

class KurzusForm(forms.ModelForm):

    kurzuskod = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Kurzus kódja"}))
    kurzusnev = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Kurzus neve"}))
    kredit = forms.IntegerField(widget=forms.TextInput(attrs={"placeholder": "Kredit értéke"}))
    teremCim = TeremForm()
    oktatoAzonosito = FelhasznaloForm()

    class Meta:
        model = Kurzus
        fields = [
            'kurzuskod',
            'kurzusnev',
            'kredit',
            'teremCim',
            'oktatoAzonosito',
        ]

