from django.db import models


# Create your models here.
class Alumne(models.Model):
    nom = models.CharField(max_length=100)
    cognoms = models.CharField(max_length=200)
    num_tlf = models.BigIntegerField()
    sexe = models.CharField(blank=True, null=True, max_length=30)

    def __str__(self):
        return f"{self.nom} {self.cognoms}"


class Nota(models.Model):
    qualificacio = models.FloatField()
    alumne = models.ForeignKey(Alumne, on_delete=models.RESTRICT, related_name="notes")

    def __str__(self):
        return f"{self.alumne} - {self.qualificacio}"
