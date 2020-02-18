from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView

from app.api.department.serializers import DepartmentSerializer
from app.model import Department


class DepartmentCreateAPIView(CreateAPIView):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()


class DepartmentUpdateAPIView(UpdateAPIView):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()
    lookup_url_kwarg = 'id'


class DepartmentDestroyAPIView(DestroyAPIView):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()
    lookup_url_kwarg = 'id'