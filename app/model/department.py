from django.db import models


class Department(models.Model):
    name = models.TextField(blank=True, null=True)