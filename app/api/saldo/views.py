from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from app.api.saldo.serializers import SaldoSerializer
from app.model import Saldo


class SaldoCreateAPIView(CreateAPIView):
    queryset = Saldo.objects.all()
    serializer_class = SaldoSerializer

    # def post(self, request, *args, **kwargs):
    #     q_code = request.POST.get('id')
    #     sp = request.POST.get('spravichnik')
    #     da = request.POST.get('date')
    #     t = request.POST.get('tick')
    #     print('ID:', q_code)
    #     s = Saldo.objects.get(id=q_code)
    #     s_count = s.count()
    #     if s_count==0:
    #         saldo = Saldo.objects.create(spravichnik=sp, date=da, tick=t)
    #
    #     print('COUNTING ', s_count)
    #     return Response(status=200)

