from django.db import models
from django.urls import reverse
from kurzus.models import Kurzus


class Elofeltetel(models.Model):

    kurzusKod = models.ForeignKey(Kurzus, null=False, db_column="kurzusKod", on_delete=models.CASCADE, related_name="kurzusKod")
    elofeltetelKod = models.ForeignKey(Kurzus, null=False, db_column="elofeltetelKod", on_delete=models.CASCADE, related_name="elofeltetelKod")

    class Meta:
        unique_together = ['kurzusKod', 'elofeltetelKod']
        db_table = "elofeltetel"

    def get_absolute_url(self):
        return reverse("elofeltetel-detail", kwargs={'elofeltetel_id': self.id})
