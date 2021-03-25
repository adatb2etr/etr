from django.db import models
from django.urls import reverse
from vizsga.models import Vizsga
from user.models import Hallgato
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_jegy(value):
    if value < 1 or value > 5:
        raise ValidationError(
            _('A jegynek 1 és 5 között kell lennie!'),
            params={'value': value},
        )

def validate_alkalom(value):
    if value < 1 or value > 3:
        raise ValidationError(
            _('A jegynek 1 és 3 között kell lennie!'),
            params={'value': value},
        )

class Vizsgazik(models.Model):

    vizsgaID = models.ForeignKey(Vizsga, on_delete=models.CASCADE, db_column="vizsgaID")
    hallgatoAzonosito = models.ForeignKey(Hallgato, on_delete=models.CASCADE, db_column="hallgatoAzonosito")
    kapottjegy = models.IntegerField(null=False, validators=[validate_jegy])
    vizsgaalkalom = models.IntegerField(null=False, validators=[validate_alkalom])

    class Meta:
        db_table = "vizsgazik"
        unique_together = ('vizsgaID', 'hallgatoAzonosito')

    def get_absolute_url(self):
        return reverse("vizsgazik-detail", kwargs={'vizsgazikID': self.id})