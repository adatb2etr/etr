from django import forms
from user.forms import FelhasznaloForm
from .models import Osztondij


class OsztondijForm(forms.ModelForm):

    hallgatoAzonosito = FelhasznaloForm()
    osztondijOsszege = forms.IntegerField(widget=forms.TextInput(attrs={"placeholder": "Ösztöndíj Összege"}))

    class Meta:
        model = Osztondij
        fields = [
            'hallgatoAzonosito',
            'osztondijOsszege',
        ]



class OsztondijFormUpdate(OsztondijForm):

    def __init__(self, *args, **kwargs):
        super(OsztondijFormUpdate, self).__init__(*args, **kwargs)
        self.fields['hallgatoAzonosito'].disabled = True