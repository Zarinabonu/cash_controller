from rest_framework.serializers import ModelSerializer, raise_errors_on_nested_writes

from app.model import Department


class DepartmentSerializer(ModelSerializer):
    class Meta:
        model = Department
        fields = ('name',
                  )

    def update(self, instance, validated_data):
        raise_errors_on_nested_writes('update', self, validated_data)

        # dept_name = validated_data.get('dept_name')
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        # instance.department = dept_name
        instance.save()

        return instance

