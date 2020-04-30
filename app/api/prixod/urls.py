from django.urls import path

from app.api.prixod import views

urlpatterns = [
    path('create', views.IncomeCreateAPIView.as_view(), name='api-prixod-create'),
    path('update/<int:id>', views.IncomeUpdateAPIView.as_view(), name='api-prixod-update'),
    path('destroy/<int:id>', views.IncomeDestroyAPIView.as_view(), name='api-prixod-destroy')

]