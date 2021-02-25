from django.contrib.auth.models import AbstractBaseUser
from django.db import models

class EtrAdmin(models.Model):

    azonosito = models.CharField(max_length=32, primary_key=True, null=False)
    vezeteknev = models.CharField(max_length=64, null=False)
    keresztnev = models.CharField(max_length=64, null=False)
    telefonszam = models.CharField(max_length=64, null=False)
    email = models.CharField(max_length=64, null=False)
    jelszo = models.CharField(max_length=64, null=False)

    class Meta:
        db_table = "etradmin"  #melyik táblába pakolja

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


class Hallgato(models.Model):

    azonosito = models.CharField(max_length=32, primary_key=True, null=False)
    vezeteknev = models.CharField(max_length=64, null=False)
    keresztnev = models.CharField(max_length=64, null=False)
    szemelyiszam = models.CharField(max_length=64, null=False)
    telefonszam = models.CharField(max_length=64, null=False)
    email = models.CharField(max_length=64, null=False)
    jelszo = models.CharField(max_length=64, null=False)
    szulido = models.DateField(null=False)

    class Meta:
        db_table = "hallgato"  #melyik táblába pakolja