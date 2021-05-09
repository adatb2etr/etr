from django.db import models
from django.urls import reverse
# Create your models here.

class Info(models.Model):

    id = models.AutoField(primary_key=True, db_column="id")
    cim = models.CharField(max_length=200, null=False)
    uzenet = models.CharField(max_length=50, null=False)
    
    class Meta:
        db_table = "infosheet"

    def __str__(self):
        return str(self.cim + " című info.")
    
    def get_absolute_url(self):
        return reverse("info-detail", kwargs={'info_id': self.id})