from django.db import models
from django.urls import reverse
from user.models import Hallgato


class Osztondij(models.Model):

    hallgatoAzonosito = models.OneToOneField(Hallgato, null=False, db_column="hallgatoAzonosito", on_delete=models.CASCADE, unique=True)
    osztondijosszeg = models.IntegerField(default=0, primary_key=True, unique=False)

    class Meta:
        db_table = "osztondij"

    def get_absolute_url(self):
        return reverse("osztondij-detail", kwargs={'hallgatoAzonositoOsztondij': self.hallgatoAzonosito.azonosito})
