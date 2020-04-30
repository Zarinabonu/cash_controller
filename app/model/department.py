from django.contrib.auth.models import User
from django.db import models


class Department(models.Model):
    name = models.TextField()
    password = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

