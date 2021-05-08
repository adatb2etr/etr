from django import forms
from .models import Kepzes


class KepzesForm(forms.ModelForm):

    kepzesid = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Képzés ID-ja"}))
    nev = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Képzés Neve"}))

    class Meta:
        model = Kepzes
        fields = [
            'kepzesid',
            'nev',
        ]



class KepzesFormUpdate(KepzesForm):

    def __init__(self, *args, **kwargs):
        super(KepzesFormUpdate, self).__init__(*args, **kwargs)
        self.fields['kepzesid'].disabled = True