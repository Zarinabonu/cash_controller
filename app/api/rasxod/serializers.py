from fnmatch import translate

from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, raise_errors_on_nested_writes

from app.model import Main, Spravichnik


class MainSerializer(ModelSerializer):
    prixod = serializers.IntegerField(write_only=True)

    class Meta:
        model = Main
        fields = ('prixod',
                  'summa',
                  'date_main',
                  'provodka',
                  )

    def create(self, validated_data):
        pri = validated_data.pop('prixod')
        main = Main(**validated_data)
        request = self.context['request']
        sum = validated_data.get('summa')
        # summ = sum.str.replace(',', '')
        # print('api summa is ', sum)
        # summ = translate(sum(',', '.'))
        # print('api222 summa is ', summ)

        prixod = Spravichnik.objects.get(id=pri)
        rasxod = Spravichnik.objects.get(department__user=request.user)
        print('prixod IS', prixod)
        print('rasxod IS', rasxod)

        main.prixod = prixod
        main.rasxod = rasxod
        main.save()
        return main

    def update(self, instance, validated_data):
        raise_errors_on_nested_writes('update', self, validated_data)

        pri = validated_data.get('prixod')
        summa = validated_data.get('summa')
        provodka = validated_data.get('provodka')
        date_main = validated_data.get('date_main')
        if instance.active==True:
            if pri:
                p = Spravichnik.objects.get(id=pri)
                instance.prixod = p
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


