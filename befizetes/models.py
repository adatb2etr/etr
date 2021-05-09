from django.db import models
from django.urls import reverse
from user.models import Hallgato


class Befizetes(models.Model):

    hallgatoAzonosito = models.OneToOneField(Hallgato, null=False, db_column="hallgatoAzonosito", on_delete=models.CASCADE, unique=True)
    befizetesosszeg = models.IntegerField(default=0, unique=False)
    datum = models.DateTimeField(null=False, auto_now_add=True)

    class Meta:
        db_table = "befizetes"

    def get_absolute_url(self):
        return reverse("befizetes-detail", kwargs={'befizetesID': self.id})
