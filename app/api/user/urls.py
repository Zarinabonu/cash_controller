from django.urls import path

from app.api.user import views

urlpatterns = [
    path('create', views.UserCreateAPIView.as_view(), name='api-user-create'),
    path('update/<int:id>', views.DepartmentUpdateAPIView.as_view(), name='api-dept-update'),

]