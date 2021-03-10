from django.db import models
from django.urls import reverse

class Terem(models.Model):

    cim = models.CharField(max_length=64, null=False, primary_key=True)
    kapacitas = models.IntegerField(default=999, null=False)

    class Meta:
        db_table = "terem"

    def get_absolute_url(self):
        return reverse("terem-detail", kwargs={'terem_cim': self.cim})