from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView

from app.api.spravichnik.serializers import SpravichnikSerializer
from app.model import Spravichnik


class SpravichnikCreateAPIView(LoginRequiredMixin,CreateAPIView):
    serializer_class = SpravichnikSerializer
    queryset = Spravichnik.objects.all()


class SpravichnikUpdateAPIView(LoginRequiredMixin, UpdateAPIView):
    serializer_class = SpravichnikSerializer
    queryset = Spravichnik.objects.all()
    lookup_url_kwarg = 'id'


class SpravichnikDestroyAPIView(LoginRequiredMixin, DestroyAPIView):
    serializer_class = SpravichnikSerializer
    queryset = Spravichnik.objects.all()
    lookup_url_kwarg = 'id'