from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from app.model import Spravichnik, Main


class Saldo(models.Model):
    spravichnik = models.ForeignKey(Spravichnik, on_delete=models.SET_NULL, null=True)
    date = models.DateField(blank=True, null=True)
    tick = models.BooleanField(default=False)
    count = models.IntegerField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)


# @receiver(post_save, sender=Saldo)
# def create_saldo(sender, instance, created, **kwargs):
#     if created:
#         y = instance.date.year
#         m = instance.date.month
#         main = Main.objects.filter(date__year=y).filter(date__month=m)
#         main.active = False
#         main.save



