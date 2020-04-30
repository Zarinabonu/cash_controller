from django.contrib import admin
from .model import Main, Spravichnik, Saldo, Department

admin.site.register(Main)
admin.site.register(Spravichnik)
admin.site.register(Saldo)
admin.site.register(Department)

# Register your models here.
