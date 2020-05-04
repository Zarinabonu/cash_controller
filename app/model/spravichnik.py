from django.contrib.auth.models import User
from django.db import models

from app.model.department import Department


class Spravichnik(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    rs = models.TextField(blank=True, null=True)
    inn = models.TextField(blank=True, null=True)
    start_FIO = models.TextField(blank=True, null=True)
    MFO = models.TextField(blank=True, null=True)

    # def __str__(self):
    #     return self.department.name

    # def __str__(self):
    #     return self.user.username