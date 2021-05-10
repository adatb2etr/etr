from django import forms
from .models import HallgatoUzenet, Tema

class HallgatoCommentForm(forms.ModelForm):

    comment = HallgatoUzenet.uzenet

    class Meta:
        model = HallgatoUzenet
        fields = [
            'uzenet',
            'tema',
            'userId',
            'valaszId',
        ]

class TemaFelvitelForm(forms.ModelForm):

    nev = Tema.nev

    class Meta:
        model = Tema
        fields = ['nev']