from django.db import models
from django.urls import reverse
from kurzus.models import Kurzus


class Vizsga(models.Model):

    vizsgaID = models.AutoField(primary_key=True, db_column="vizsgaID")
    kurzusKod = models.ForeignKey(Kurzus, on_delete=models.CASCADE, db_column="kurzusKod")
    idopont = models.DateTimeField(null=False)
    ferohely = models.IntegerField(null=False, default=999)

    class Meta:
        db_table = "vizsga"

    def __str__(self):
        return str(self.idopont) + "  (" + self.kurzusKod.kurzuskod + ")"

    def get_absolute_url(self):
        return reverse("vizsga-detail", kwargs={'vizsgaID': self.vizsgaID})