from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView, UpdateAPIView

from app.api.user.serializers import UserSerializer
from app.model import Department


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = Department.objects.all()


class DepartmentUpdateAPIView(UpdateAPIView):
    serializer_class = UserSerializer
    queryset = Department.objects.all()
    lookup_url_kwarg = 'id'

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)


