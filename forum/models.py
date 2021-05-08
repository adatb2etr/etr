from django.db import models
from django.urls import reverse
from user.models import Oktato, Hallgato

class Tema(models.Model):

    nev = models.CharField(primary_key=True, max_length=20, null=False)
    
    class Meta:
        db_table = "tema"

    def __str__(self):
        return str(self.nev)

class OktatoUzenet(models.Model):

    id = models.AutoField(primary_key=True, db_column="id", default=0)
    uzenet = models.CharField(max_length=20, null=False)
    datum = models.DateTimeField(max_length=20, null=False)    
    tema = models.ForeignKey(Tema, blank=True, null=True, on_delete=models.CASCADE, db_column="temaNev")
    userId = models.ForeignKey(Oktato, max_length=6, null=True, on_delete=models.CASCADE, db_column="oktatoAzonosito", blank=True)
    
    class Meta:
        db_table = "forumOktato"

    def __str__(self):
        return str(self.uzenet + " (" + self.datum + ")")

class HallgatoUzenet(models.Model):

    id = models.AutoField(primary_key=True, db_column="id", default=0)
    uzenet = models.CharField(max_length=20, null=False)
    datum = models.DateTimeField(max_length=20, null=False)    
    tema = models.ForeignKey(Tema, blank=True, null=True, on_delete=models.CASCADE, db_column="temaNev")
    userId = models.ForeignKey(Hallgato, max_length=6, null=True, on_delete=models.CASCADE, db_column="hallgatoAzonosito", blank=True)
    
    class Meta:
        db_table = "forumHallgato"

    def __str__(self):
        return str(self.uzenet)