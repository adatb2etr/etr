from django.db import models
from django.urls import reverse
from kurzus.models import Kurzus

class Idopont(models.Model):

    kezdete = models.DateTimeField(null=False)
    vege = models.DateTimeField(null=False)
    kurzusKod = models.ForeignKey(Kurzus, null=False, db_column="kurzusKod", on_delete=models.CASCADE)

    class Meta:
        db_table = "idopont"
        unique_together = ("kezdete", "vege", "kurzusKod")

    def get_absolute_url(self):
        return reverse("idopont-detail", kwargs={'idopont_id': self.id})

