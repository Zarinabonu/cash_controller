from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from app.model import Saldo, Spravichnik


class SaldoSerializer(ModelSerializer):
    spravichnik = serializers.IntegerField(write_only=True)

    class Meta:
        model = Saldo
        fields = ('spravichnik',
                  'date',
                  'tick')

    def create(self, validated_data):
        sp = validated_data.pop('spravichnik')

        saldo = Saldo(**validated_data)
        s = Spravichnik.objects.get(id=sp)
        saldo.spravichnik = s
        saldo.save()

        return saldo