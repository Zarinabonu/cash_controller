from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView

from app.api.prixod.serializers import IncomeSerializer
from app.api.rasxod.serializers import MainSerializer
from app.model import Main


class IncomeCreateAPIView(LoginRequiredMixin, CreateAPIView):
    serializer_class = IncomeSerializer
    queryset = Main.objects.all()


class IncomeUpdateAPIView(LoginRequiredMixin, UpdateAPIView):
    serializer_class = IncomeSerializer
    queryset = Main.objects.all()
    lookup_url_kwarg = 'id'


class IncomeDestroyAPIView(LoginRequiredMixin, DestroyAPIView):
    serializer_class = IncomeSerializer
    queryset = Main.objects.all()
    lookup_url_kwarg = 'id'