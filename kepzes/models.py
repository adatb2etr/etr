from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from django.urls import reverse

class Kepzes(models.Model):

    kepzesid = models.CharField(max_length=64, primary_key=True, null=False)
    nev = models.CharField(max_length=64, null=False)

    class Meta:
        db_table = "kepzes"  #melyik táblába pakolja

    def get_absolute_url(self):
        return reverse("kepzes-detail", kwargs={"kepzesid": self.kepzesid})
