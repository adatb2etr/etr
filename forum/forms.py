from django import forms
from .models import HallgatoUzenet

class HallgatoCommentForm(forms.ModelForm):

    comment = HallgatoUzenet.uzenet

    class Meta:
        model = HallgatoUzenet
        fields = [
            'uzenet',
            'tema',
            'userId',
        ]