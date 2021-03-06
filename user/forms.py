from django import forms

from user.models import EtrAdmin, Oktato, Hallgato

class EtrAdminForm(forms.ModelForm):
    azonosito = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Azonosito"}))
    vezeteknev = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Vezeteknev"}))
    keresztnev = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Keresztnev"}))
    telefonszam = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Telefonszam"}))
    email = forms.EmailField(widget=forms.TextInput(attrs={"placeholder": "Email"}))
    jelszo = forms.CharField(widget=forms.PasswordInput())
    jelszo2 = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = EtrAdmin
        fields = [
            'azonosito',
            'vezeteknev',
            'keresztnev',
            'telefonszam',
            'email',
            'jelszo',
            'jelszo2',
        ]

class FelhasznaloForm(forms.ModelForm):

    vezeteknev = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Vezeteknev"}))
    keresztnev = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Keresztnev"}))
    szemelyiszam = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Keresztnev"}))
    telefonszam = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Telefonszam"}))
    email = forms.EmailField(widget=forms.TextInput(attrs={"placeholder": "Email"}))
    jelszo = forms.CharField(widget=forms.PasswordInput())
    jelszo2 = forms.CharField(widget=forms.PasswordInput())
    szulido = forms.DateField()
    Oktato = forms.BooleanField(required=False)
    Hallgato = forms.BooleanField(required=False)
    class Meta:
        model = Oktato  # muszáj ide írni
        fields = [
            'vezeteknev',
            'keresztnev',
            'szemelyiszam',
            'telefonszam',
            'email',
            'jelszo',
            'jelszo2',
            'szulido',
            'Oktato',
            'Hallgato',
        ]