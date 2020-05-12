from django.db import models

from app.model.spravichnik import Spravichnik


class Main(models.Model):
    prixod = models.ForeignKey(Spravichnik, on_delete=models.CASCADE, related_name='prixod')
    rasxod = models.ForeignKey(Spravichnik, on_delete=models.CASCADE, related_name='rasxod')
    summa = models.FloatField(blank=True, null=True)
    provodka = models.TextField(null=True, blank=True)
    active = models.BooleanField(default=True)
    date = models.DateField()

    def __str__(self):
        return self.prixod.department.name

    def __str__(self):
        return self.rasxod.department.name


# class Rasxod(models.Model):
#     rasxod = models.ForeignKey(Spravichnik, on_delete=models.CASCADE, related_name='rasxod')
#     summa = models.FloatField(blank=True, null=True)
#     provodka = models.TextField(null=True, blank=True)
#     active = models.BooleanField(default=True)
#
#     # def __str__(self):
#     #     return self.rasxod.department.name
#
#
# class Main(models.Model):
#     rasxod = models.ForeignKey(Rasxod, on_delete=models.CASCADE, related_name='rasxod_main')
#     prixod = models.ForeignKey(Prixod, on_delete=models.CASCADE, related_name='prixod_main')
#     date = models.DateField()

    # def __str__(self):
    #     return self.rasxod.department.name
    #
    # def __str__(self):
    #     return self.prixod.department.name

