from rest_framework.generics import CreateAPIView

from app.api.saldo.serializers import SaldoSerializer
from app.model import Saldo


class SaldoCreateAPIView(CreateAPIView):
    queryset = Saldo.objects.all()
    serializer_class = SaldoSerializer