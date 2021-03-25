from django.db import models
from django.urls import reverse
from user.models import Oktato
from terem.models import Terem
class Kurzus(models.Model):

    kurzuskod = models.CharField(max_length=20, null=False, primary_key=True)
    kurzusnev = models.CharField(max_length=64, null=False)
    ferohely = models.IntegerField(default=999, null=False)
    kredit = models.IntegerField(default=1, null=False)
    teremCim = models.ForeignKey(Terem, null=False, on_delete=models.CASCADE, db_column="teremCim")
    oktatoAzonosito = models.ForeignKey(Oktato, max_length=6, null=True, on_delete=models.CASCADE, db_column="oktatoAzonosito", blank=True)

    class Meta:
        db_table = "kurzus"

    def __str__(self):
        return str(self.kurzusnev + " (" + self.kurzuskod + ")")

    def get_absolute_url(self):
        return reverse("kurzus-detail", kwargs={'kurzus_kod': self.kurzuskod})
