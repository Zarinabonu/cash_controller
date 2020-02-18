from django.urls import path

from app.api.spravichnik import views

urlpatterns = [
    path('create', views.SpravichnikCreateAPIView.as_view(), name='api-spravichnik-create'),
    path('update/<int:id>', views.SpravichnikUpdateAPIView.as_view(), name='api-spravichnik-update'),
    path('destroy/<int:id>', views.SpravichnikDestroyAPIView.as_view(), name='api-spravichnik-destroy'),

]