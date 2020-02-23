from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, raise_errors_on_nested_writes

from app.model import Spravichnik, Department


class SpravichnikSerializer(ModelSerializer):
    # department = serializers.DepartmentSerializer(read_only=True)
    department = serializers.IntegerField(write_only=True)

    class Meta:
        model = Spravichnik
        fields = ('department',
                  'rs',
                  'inn',
                  'start_FIO',
                  'password',
                  'MFO')

    def create(self, validated_data):
        dept = validated_data.pop('department')
        d = Department.objects.get(id=dept)
        s = Spravichnik(**validated_data)
        s.department = d
        s.save()
        return s

    def update(self, instance, validated_data):
        raise_errors_on_nested_writes('update', self, validated_data)

        dept = validated_data.get('department')
        rs = validated_data.get('rs')
        inn = validated_data.get('inn')
        password = validated_data.get('password')
        start_FIO = validated_data.get('start_FIO')
        MFO = validated_data.get('MFO')

        if dept:
            d = Department.objects.get(id=dept)
            instance.department = d
            instance.save()
        if rs:
            instance.rs = rs
            instance.save()
        if inn:
            instance.inn = inn
            instance.save()
        if password:
            instance.password = password
            instance.save()
        if start_FIO:
            instance.start_FIO = start_FIO
            instance.save()
        if MFO:
            instance.MFO = MFO
            instance.save()

        # for attr, value in validated_data.items():
        #     setattr(instance, attr, value)

        instance.save()

        return instance



        # if dept:
        #     d = Department.objects.get(id=dept)
        #     instance.department = d
        #     instance.save()
        # elif rs:
        #     instance.rs = rs
        #     instance.save()
        # elif inn:
        #     instance.inn = inn
        #     instance.save()
        # elif passwrord:
        #     instance.password = passwrord
        #     instance.save()
        # elif start_FIO:
        #     instance.start_FIO = start_FIO
        #     instance.save()
        # elif MFO:
        #     instance.MFO = MFO
        #     instance.save()
        #
        # return instance

