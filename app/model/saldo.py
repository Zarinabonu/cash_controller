from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from app.model import Spravichnik, Main


class Saldo(models.Model):
    spravichnik = models.ForeignKey(Spravichnik, on_delete=models.SET_NULL, null=True)
    date = models.DateField(blank=True, null=True)
    tick = models.BooleanField(default=False)
    count_saldo = models.IntegerField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)


@receiver(post_save, sender=Saldo)
def create_saldo(sender, instance, created, **kwargs):
    ras = 0
    pri = 0

    if created:
        r = Main.objects.filter(rasxod=instance.spravichnik).filter(date__year=instance.date.year).filter(date__month=instance.date.month)
        p = Main.objects.filter(prixod=instance.spravichnik).filter(date__year=instance.date.year).filter(date__month=instance.date.month)

        for item in r:
            ras += item.summa
            item.active = False
            item.save()
        print('object is ', r, ' RASXOD is ', ras)

        for pr in p:
            pri += pr.summa
        check = Saldo.objects.filter(spravichnik=instance.spravichnik)
        # check_s = check.count(id)
        print('check saldo: ', check.count())
        # if not check.count()==0:
        if instance.date.month == 1:
            s = Saldo. objects.filter(spravichnik=instance.spravichnik).filter(date__year=instance.date.year - 1).filter(date__month=12)
        else:
            s = Saldo.objects.filter(spravichnik=instance.spravichnik).filter(date__year=instance.date.year).filter(date__month=instance.date.month - 1)
        if check.count() > 1:
            instance.count_saldo = s.first().count_saldo + pri - ras
            instance.save()
        return  instance

        # print(' object is ', r, ' PRIXOD is ', pri)






