from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from app.model import Saldo, Spravichnik


class SaldoSerializer(ModelSerializer):
    # spravichnik = serializers.IntegerField(write_only=True)

    class Meta:
        model = Saldo
        fields = ('date_saldo',
                  'tick')

    def create(self, validated_data):
        # sp = validated_data.pop('spravichnik')

        saldo = Saldo(**validated_data)
        request = self.context['request']
        print('REQUEST USER', request.user.username)
        us = User.objects.get(username=request.user.username)
        ras = Spravichnik.objects.get(user=us)
        saldo.spravichnik = ras
        saldo.save()

        return saldo