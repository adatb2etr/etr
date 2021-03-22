from django.db import models
from django.urls import reverse
from user.models import Hallgato
from kurzus.models import Kurzus


class Kurzustfelvesz(models.Model):

    hallgatoAzonosito = models.ForeignKey(Hallgato, null=False, db_column="hallgatoAzonosito", on_delete=models.CASCADE)
    kurzusKod = models.ForeignKey(Kurzus, null=False, db_column="kurzusKod", on_delete=models.CASCADE)
    teljesitette = models.IntegerField(null=False, default=0)

    class Meta:
        db_table = "kurzustfelvesz"

    def get_absolute_url(self):
        return reverse("kurzustfelvesz-detail", kwargs={'kurzustfelvesz_id': self.id})
