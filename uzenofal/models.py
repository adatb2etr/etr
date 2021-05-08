from django.db import models

# Create your models here.

class Uzenet(models.Model):

    id = models.AutoField(primary_key=True, db_column="id", default=0)
    cim = models.CharField(max_length=20, null=False)
    uzenet = models.CharField(max_length=50, null=False)
    
    class Meta:
        db_table = "uzenofal"

    def __str__(self):
        return str(self.cim + " című info.")
    
    def get_absolute_url(self):
        return reverse("uzenet-detail", kwargs={'uzenet_id': self.id})