from django.urls import path

from app.api.rasxod import views

urlpatterns = [
    path('create', views.MainCreateAPIView.as_view(), name='api-rasxod-create'),
    path('update/<int:id>', views.MainUpdateAPIView.as_view(), name='api-rasxod-update'),
    path('destroy/<int:id>', views.MainDestroyAPIView.as_view(), name='api-rasxod-destroy')

]