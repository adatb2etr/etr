from django.db import models
from django.urls import reverse
from kurzus.models import Kurzus
from kepzes.models import Kepzes


class Teljesitesfeltetel(models.Model):

    kepzesId = models.OneToOneField(Kepzes, null=False, db_column="kepzesId", on_delete=models.CASCADE, unique=True)
    kurzusKod = models.OneToOneField(Kurzus, null=False, db_column="kurzusKod", on_delete=models.CASCADE, unique=True)

    class Meta:
        db_table = "teljesitesfeltetel"

    def get_absolute_url(self):
        return reverse("teljesitesfeltetel-detail", kwargs={'teljesitesfeltetelID': self.id})
