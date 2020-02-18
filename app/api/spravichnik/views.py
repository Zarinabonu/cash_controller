from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView

from app.api.spravichnik.serializers import SpravichnikSerializer
from app.model import Spravichnik


class SpravichnikCreateAPIView(CreateAPIView):
    serializer_class = SpravichnikSerializer
    queryset = Spravichnik.objects.all()


class SpravichnikUpdateAPIView(UpdateAPIView):
    serializer_class = SpravichnikSerializer
    queryset = Spravichnik.objects.all()
    lookup_url_kwarg = 'id'


class SpravichnikDestroyAPIView(DestroyAPIView):
    serializer_class = SpravichnikSerializer
    queryset = Spravichnik.objects.all()
    lookup_url_kwarg = 'id'