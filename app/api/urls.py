from django.urls import include, path

urlpatterns = [
    path('dept/', include('app.api.department.urls')),
    path('spravichnik/', include('app.api.spravichnik.urls')),
    path('main/', include('app.api.main.urls')),
    path('saldo/', include('app.api.saldo.urls')),

]