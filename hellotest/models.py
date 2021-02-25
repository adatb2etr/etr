from django.db import models

# Create your models here.
from django.core.validators import RegexValidator


class Hellotest(models.Model):
    alphanumeric = RegexValidator(r'^[0-9a-zA-Z\s]*$', 'Csak az angol abc betui illetve szamok megengedettek!')

    COLUMN1 = models.CharField(primary_key=True, max_length=20, validators=[alphanumeric])
    class Meta:
        db_table = "HELLOTEST"  #melyik táblába pakolja



def testimport():
    Hellotest.objects.create(COLUMN1="Teszt2")
    Hellotest.objects.filter(COLUMN1="Teszt2").delete()

