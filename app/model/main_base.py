from django.db import models

from app.model.spravichnik import Spravichnik


class Main(models.Model):
    rasxod = models.ForeignKey(Spravichnik, on_delete=models.CASCADE, related_name='rasxod')
    prixod = models.ForeignKey(Spravichnik, on_delete=models.CASCADE, related_name='prixod')
    summa = models.IntegerField(blank=True, null=True)
    date = models.DateField()
    provodka = models.TextField(null=True, blank=True)
    active = models.BooleanField(default=True)