from django.urls import path

from app.api.saldo import views

urlpatterns = [
    path('create', views.SaldoCreateAPIView.as_view(), name='api-saldo-create'),

]