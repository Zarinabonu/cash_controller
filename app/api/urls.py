from django.urls import include, path

urlpatterns = [
    path('spravichnik/', include('app.api.spravichnik.urls')),
    path('rasxod/', include('app.api.rasxod.urls')),
    path('saldo/', include('app.api.saldo.urls')),
    path('prixod/', include('app.api.prixod.urls')),
    path('dept/', include('app.api.user.urls')),

]