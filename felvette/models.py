from django.db import models
from django.urls import reverse
from user.models import Hallgato
from kepzes.models import Kepzes


class Felvette(models.Model):

    hallgatoAzonosito = models.OneToOneField(Hallgato, null=False, db_column="hallgatoAzonosito", on_delete=models.CASCADE, unique=True)
    kepzesId = models.OneToOneField(Kepzes, null=False, db_column="kepzesId", on_delete=models.CASCADE, unique=True)
    teljesitette = models.IntegerField(default=0, null=False)

    class Meta:
        db_table = "felvette"

    def get_absolute_url(self):
        return reverse("felvette-detail", kwargs={'felvetteID': self.id})
