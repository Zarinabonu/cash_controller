from django.urls import path

from app.api.department import views

urlpatterns = [
    path('create', views.DepartmentCreateAPIView.as_view(), name='api-dept-create'),
    path('update/<int:id>', views.DepartmentUpdateAPIView.as_view(), name='api-dept-update'),
    path('destroy/<int:id>', views.DepartmentDestroyAPIView.as_view(), name='api-dept-destroy'),

]