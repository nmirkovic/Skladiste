from django.db import models
from datetime import datetime


class Artikl(models.Model):
    naziv_artikla = models.CharField("naziv artikla", max_length=30)
    opis_artikla = models.CharField("opis artikla", max_length=30)

    def __str__(self):
        return self.naziv_artikla


class JedinicaMjere(models.Model):
    naziv_mjere = models.CharField("naziv mjere", max_length=25)
    oznaka = models.CharField("oznaka", max_length=5)

    def __str__(self):
        return self.naziv_mjere


class Lokacija(models.Model):
    naziv_lokacije = models.CharField("naziv lokacije", max_length=5)
    opis_lokacije = models.CharField("opis lokacije", max_length=100)

    def __str__(self):
        return self.naziv_lokacije


class Stanje(models.Model):
    artikl_id = models.ForeignKey(Artikl, on_delete=models.CASCADE)
    lokacija_id = models.ForeignKey(Lokacija, on_delete=models.CASCADE)
    jedinica_mjere_id = models.ForeignKey(JedinicaMjere, on_delete=models.CASCADE)
    kolicina = models.IntegerField(null=True)
    datum = models.DateTimeField(default=datetime.now)
