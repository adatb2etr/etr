from django.db import models
from django.urls import reverse
from user.models import Hallgato


class Tartozas(models.Model):

    hallgatoAzonosito = models.OneToOneField(Hallgato, null=False, db_column="hallgatoAzonosito", on_delete=models.CASCADE, unique=True)
    tartozasosszeg = models.IntegerField(default=0, primary_key=True, unique=False)

    class Meta:
        db_table = "tartozas"

    def get_absolute_url(self):
        return reverse("tartozas-detail", kwargs={'hallgatoAzonosito': self.hallgatoAzonosito.azonosito})
