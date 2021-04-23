from django import forms

from user.models import EtrAdmin, Oktato, Hallgato

class DateInput(forms.DateInput):
    input_type = 'date'

ACCOUNT_TYPE = ((1, "Hallgató"), (2, "Oktató"))

class EtrAdminForm(forms.ModelForm):
    azonosito = forms.CharField(label="Azonosító:", widget=forms.TextInput(attrs={"placeholder": "Azonosító"}))
    vezeteknev = forms.CharField(label="Vezetéknév:", widget=forms.TextInput(attrs={"placeholder": "Vezetéknév"}))
    keresztnev = forms.CharField(label="Keresztnév:", widget=forms.TextInput(attrs={"placeholder": "Keresztnév"}))
    telefonszam = forms.CharField(label="Telefonszám:", widget=forms.TextInput(attrs={"placeholder": "Telefonszám"}))
    email = forms.EmailField(label="E-mail cím:", widget=forms.TextInput(attrs={"placeholder": "Email-cím"}))
    jelszo = forms.CharField(label="Jelszó:", widget=forms.PasswordInput(attrs={"placeholder": "Jelszó"}))
    jelszo2 = forms.CharField(label="Jelszó újra:", widget=forms.PasswordInput(attrs={"placeholder": "Jelszó újra"}))

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
    vezeteknev = forms.CharField(label="Vezetéknév:", widget=forms.TextInput(attrs={"id": "vezeteknev", "class": "form-control" ,"placeholder": "Vezeteknev"}))
    keresztnev = forms.CharField(label="Keresztnév:", widget=forms.TextInput(attrs={"id": "keresztnev", "class": "form-control" ,"placeholder": "Keresztnev"}))
    szemelyiszam = forms.CharField(label="Személyiszám:", widget=forms.TextInput(attrs={"id": "szemelyiszam", "class": "form-control" ,"placeholder": "Keresztnev"}))
    telefonszam = forms.CharField(label="Telefonszám:", widget=forms.TextInput(attrs={"id": "telefonszam", "class": "form-control" ,"placeholder": "Telefonszam"}))
    email = forms.EmailField(label="E-mail cím:", widget=forms.TextInput(attrs={"id": "email", "class": "form-control" ,"placeholder": "Email"}))
    jelszo = forms.CharField(label="Jelszó:", widget=forms.PasswordInput(attrs={"id": "jelszo", "class": "form-control" ,"placeholder": "Jelszó"}))
    jelszo2 = forms.CharField(label="Jelszó megerősítése:", widget=forms.PasswordInput(attrs={"id": "jelszo2", "class": "form-control" ,"placeholder": "Jelszó megerősítése"}))
    account_type = forms.ChoiceField(label="Felhasználói fiók típusa:", choices=ACCOUNT_TYPE)
    Oktato = forms.BooleanField(label="Hallgató:", required=False, widget=forms.HiddenInput())
    Hallgato = forms.BooleanField(label="Oktató:", required=False, widget=forms.HiddenInput())

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
        widgets = {
            'szulido': DateInput(),
            'account_type': forms.Select(attrs={'class': 'bootstrap-select'}),
        }

class FelhasznaloLoginForm(forms.ModelForm):

    neptunkod = forms.CharField(label="Neptun kód:", widget=forms.TextInput(attrs={"id": "neptunkod", "class": "form-control" ,"placeholder": "Neptun-kód"}))
    jelszo = forms.CharField(label="Jelszó:", widget=forms.PasswordInput(attrs={"id": "jelszo", "class": "form-control" ,"placeholder": "Jelszó"}))
    class Meta:
        model = Oktato
        fields = [
            'neptunkod',
            'jelszo',
        ]