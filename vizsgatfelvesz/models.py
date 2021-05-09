from django.db import models
from django.urls import reverse
from user.models import Hallgato
from vizsga.models import Vizsga

class VizsgatFelvesz(models.Model):

    vizsgaID = models.ForeignKey(Vizsga, null=False, db_column="vizsgaID", on_delete=models.CASCADE)
    hallgatoAzonosito = models.ForeignKey(Hallgato, null=False, db_column="hallgatoAzonosito", on_delete=models.CASCADE)
    erdemjegy = models.IntegerField(null=False, default=0)
    evszam = models.IntegerField(null=False, default=0)

    class Meta:
        db_table = "vizsgatfelvesz"

    def get_absolute_url(self):
        return reverse("vizsgatfelvesz-detail", kwargs={'vizsgatfelvesz_id': self.vizsgaID})
