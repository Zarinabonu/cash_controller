from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, raise_errors_on_nested_writes

from app.model import Main, Spravichnik


class MainSerializer(ModelSerializer):
    prixod = serializers.IntegerField(write_only=True)
    rasxod = serializers.IntegerField(write_only=True)

    class Meta:
        model = Main
        fields = ('prixod',
                  'rasxod',
                  'summa',
                  'date',
                  'provodka',
                  )

    def create(self, validated_data):
        pri = validated_data.pop('prixod')
        ras = validated_data.pop('rasxod')
        p = Spravichnik.objects.get(id=pri)
        r = Spravichnik.objects.get(id=ras)
        m = Main(**validated_data)
        m.prixod = p
        m.rasxod = r
        m.save()
        return m

    def update(self, instance, validated_data):
        raise_errors_on_nested_writes('update', self, validated_data)

        pri = validated_data.get('prixod')
        ras = validated_data.get('rasxod')
        summa = validated_data.get('summa')
        provodka = validated_data.get('provodka')
        date = validated_data.get('date')
        if pri:
            p = Spravichnik.objects.get(id=pri)

            instance.prixod = p
            instance.save()
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
        if date:
            instance.date = date
            instance.save()

        return instance


