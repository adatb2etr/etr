from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from django.urls import reverse

class EtrAdmin(models.Model):

    azonosito = models.CharField(max_length=32, primary_key=True, null=False)
    vezeteknev = models.CharField(max_length=64, null=False)
    keresztnev = models.CharField(max_length=64, null=False)
    telefonszam = models.CharField(max_length=64, null=False)
    email = models.CharField(max_length=64, null=False)
    jelszo = models.CharField(max_length=64, null=False)

    class Meta:
        db_table = "etradmin"  #melyik táblába pakolja

    def get_absolute_url(self):
        return reverse("etradmin-detail", kwargs={"etradmin_Azonosito": self.azonosito})

class Oktato(models.Model):

    azonosito = models.CharField(max_length=6, primary_key=True, null=False)
    vezeteknev = models.CharField(max_length=64, null=False)
    keresztnev = models.CharField(max_length=64, null=False)
    szemelyiszam = models.CharField(max_length=64, null=False)
    telefonszam = models.CharField(max_length=64, null=False)
    email = models.CharField(max_length=64, null=False)
    jelszo = models.CharField(max_length=64, null=False)
    szulido = models.DateField(null=False)

    class Meta:
        db_table = "oktato"  #melyik táblába pakolja

    def __str__(self):
        return str(self.vezeteknev + " " + self.keresztnev + " (" + self.azonosito + ")")

    def get_absolute_url(self):
        return reverse("FelhasznaloView", kwargs={"UserAzonosito": self.azonosito})


class Hallgato(models.Model):

    azonosito = models.CharField(max_length=32, primary_key=True, null=False)
    vezeteknev = models.CharField(max_length=64, null=False)
    keresztnev = models.CharField(max_length=64, null=False)
    szemelyiszam = models.CharField(max_length=64, null=False)
    telefonszam = models.CharField(max_length=64, null=False)
    email = models.CharField(max_length=64, null=False)
    jelszo = models.CharField(max_length=64, null=False)
    szulido = models.DateField(null=False)
    teljesitettkreditek = models.IntegerField(default=0, null=False)
    kepzes = models.CharField(max_length=64, null=False, default="Not_Defined")

    class Meta:
        db_table = "hallgato"  #melyik táblába pakolja

    def __str__(self):
        return str(self.vezeteknev + " " + self.keresztnev + " (" + self.azonosito + ")")

    def get_absolute_url(self):
        return reverse("FelhasznaloView", kwargs={"UserAzonosito": self.azonosito})
