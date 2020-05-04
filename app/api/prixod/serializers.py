from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, raise_errors_on_nested_writes

from app.model import Main, Spravichnik


class IncomeSerializer(ModelSerializer):
    rasxod = serializers.IntegerField(write_only=True)

    class Meta:
        model = Main
        fields = ('rasxod',
                  'summa',
                  'date_main',
                  'provodka',
                  )

    def create(self, validated_data):
        ras = validated_data.pop('rasxod')
        main = Main(**validated_data)
        rasxod = Spravichnik.objects.get(id=ras)
        request = self.context['request']
        prixod = Spravichnik.objects.get(department__user=request.user)

        main.prixod = prixod
        main.rasxod = rasxod
        main.save()
        return main

    def update(self, instance, validated_data):
        raise_errors_on_nested_writes('update', self, validated_data)

        ras = validated_data.get('rasxod')
        summa = validated_data.get('summa')
        provodka = validated_data.get('provodka')
        date_main = validated_data.get('date_main')
        if instance.active==True:
            if ras:
                p = Spravichnik.objects.get(id=ras)

                instance.rasxod = p
                instance.save()
            if summa:
                instance.summa = summa
                instance.save()
            if provodka:
                instance.provodka = provodka
                instance.save()
            if date_main:
                instance.date_main = date_main
                instance.save()

        return instance


