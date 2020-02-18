from django.urls import path

from app.api.main import views

urlpatterns = [
    path('create', views.MainCreateAPIView.as_view(), name='api-main-create'),
    path('update/<int:id>', views.MainUpdateAPIView.as_view(), name='api-main-update'),
    path('destroy/<int:id>', views.MainDestroyAPIView.as_view(), name='api-main-destroy')

]