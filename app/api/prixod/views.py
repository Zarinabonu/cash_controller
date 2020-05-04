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

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)



class IncomeDestroyAPIView(LoginRequiredMixin, DestroyAPIView):
    serializer_class = IncomeSerializer
    queryset = Main.objects.all()
    lookup_url_kwarg = 'id'