from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView

from app.api.rasxod.serializers import MainSerializer
from app.model import Main


class MainCreateAPIView(LoginRequiredMixin, CreateAPIView):
    serializer_class = MainSerializer
    queryset = Main.objects.all()


class MainUpdateAPIView(LoginRequiredMixin, UpdateAPIView):
    serializer_class = MainSerializer
    queryset = Main.objects.all()
    lookup_url_kwarg = 'id'


class MainDestroyAPIView(LoginRequiredMixin, DestroyAPIView):
    serializer_class = MainSerializer
    queryset = Main.objects.all()
    lookup_url_kwarg = 'id'