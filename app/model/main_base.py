from django.db import models

from app.model.spravichnik import Spravichnik


class Main(models.Model):
    prixod = models.ForeignKey(Spravichnik, on_delete=models.CASCADE, related_name='prixod')
    rasxod = models.ForeignKey(Spravichnik, on_delete=models.CASCADE, related_name='rasxod')
    summa = models.IntegerField(blank=True, null=True)
    date = models.DateField()
    provodka = models.TextField(null=True, blank=True)