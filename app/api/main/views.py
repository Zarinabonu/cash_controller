from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView

from app.api.main.serializers import MainSerializer
from app.model import Main


class MainCreateAPIView(CreateAPIView):
    serializer_class = MainSerializer
    queryset = Main.objects.all()


class MainUpdateAPIView(UpdateAPIView):
    serializer_class = MainSerializer
    queryset = Main.objects.all()
    lookup_url_kwarg = 'id'


class MainDestroyAPIView(DestroyAPIView):
    serializer_class = MainSerializer
    queryset = Main.objects.all()
    lookup_url_kwarg = 'id'