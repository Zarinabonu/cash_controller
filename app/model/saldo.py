from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from app.model import Spravichnik, Main


class Saldo(models.Model):
    spravichnik = models.ForeignKey(Spravichnik, on_delete=models.SET_NULL, null=True)
    date_saldo = models.DateField(blank=True, null=True)
    tick = models.BooleanField(default=False)
    count_saldo = models.FloatField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return self.spravichnik.department.name
    #
    # def __str__(self):
    #     return self.spravichnik.user.name


@receiver(post_save, sender=Saldo)
def create_saldo(sender, instance, created, **kwargs):
    ras = 0
    pri = 0

    if created:
        spravichnik = Spravichnik.objects.get(id=instance.spravichnik.id)
        print('instance spravichnik', spravichnik.id)

        r = Main.objects.filter(rasxod__id=spravichnik.id).filter(date_main__year=instance.date_saldo.year).filter(date_main__month=instance.date_saldo.month)
        # .filter(date_main__year=instance.date_saldo.year).filter(date_main__month=instance.date_saldo.month)
        p = Main.objects.filter(prixod=instance.spravichnik).filter(date_main__year=instance.date_saldo.year).filter(date_main__month=instance.date_saldo.month)
        # .filter(date_main__year=instance.date_saldo.year).filter(date_main__month=instance.date_saldo.month)
        print('11rasxodlar ', r)
        print('11prixodlar', p)
        for item in r:
            ras += item.summa
            item.active = False
            item.save()
            print('object is ', r, ' RASXOD is ', ras)
#
        for pr in p:
            pri += pr.summa
            print('prixodlar aoni', pri)
        check = Saldo.objects.filter(spravichnik=instance.spravichnik)
        # check_s = check.count(id)
        print('check saldo: ', check.count())
        # if not check.count()==0:
        if instance.date_saldo.month == 1:
            s = Saldo. objects.filter(spravichnik=instance.spravichnik).filter(date_saldo__year=instance.date_saldo.year - 1).filter(date_saldo__month=12)
        else:
            s = Saldo.objects.filter(spravichnik=instance.spravichnik).filter(date_saldo__year=instance.date_saldo.year).filter(date_saldo__month=instance.date_saldo.month - 1)
        if check.count() > 1:
            instance.count_saldo = s.first().count_saldo + pri - ras
            instance.save()
#
        return instance

        # print(' object is ', r, ' PRIXOD is ', pri)






