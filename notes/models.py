from django.db import models


# Create your models here.
class Alumne(models.Model):
    nom = models.CharField(max_length=100)
    cognoms = models.CharField(max_length=200)
    num_tlf = models.BigIntegerField()
    sexe = models.CharField(blank=True, null=True)

