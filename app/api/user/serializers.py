from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer, raise_errors_on_nested_writes

from app.model import Department


class UserSerializer(ModelSerializer):
    class Meta:
        model = Department
        fields = ('name',
                  'password')

    def create(self, validated_data):
        departmen = Department(**validated_data)
        u = User.objects.create(username=validated_data.get('name'))
        u.set_password(validated_data.get('password'))
        departmen.user = u
        departmen.save()
        u.save()
        return u

    def update(self, instance, validated_data):
        raise_errors_on_nested_writes('update', self, validated_data)

        password = validated_data.get('password')
        print('hello')

        if password:
            instance.password = password
            instance.user.set_password(password)
            print('password', instance.password, 'user password', instance.user.password)

        instance.user.save()
        instance.save()
        return instance
        #
        # password = validated_data.get('password')
        # print('password ', password)
        #
        # for attr, value in validated_data.items():
        #     setattr(instance, attr, value)
        #
        # instance.save()
        #
        # if password:
        #     print('password111 ', password)
        #
        #     instance.password = password
        #     instance.save()
        #
        # # instance.user.save()
        #
        # return instance