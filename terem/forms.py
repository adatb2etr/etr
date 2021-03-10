from django import forms

from terem.models import Terem


class TeremForm(forms.ModelForm):

    cim = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Terem címe"}))
    kapacitas = forms.IntegerField(widget=forms.TextInput(attrs={"placeholder": "Terem Max Kapacitása"}))

    class Meta:
        model = Terem
        fields = [
            'cim',
            'kapacitas',
        ]


class TeremFormUpdate(TeremForm):
                                            # itt Disable-elem a cím updateolásának a lehetőségét, mert az a
    def __init__(self, *args, **kwargs):    # Primary Key, és ha updateoljuk akkor létrehoz egy újat
        super(TeremFormUpdate, self).__init__(*args, **kwargs)
        self.fields['cim'].disabled = True