from rest_framework import serializers
from users.models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'card_id', 'first_name', 'last_name', 'email', 'mobile_number', 'balance')
        model = Employee
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = Employee(**validated_data)
        user.set_password(password)
        user.save()
        Employee.objects.create(user=user)

        return user

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.card_id = validated_data.get('card_id', instance.card_id)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.mobile_number = validated_data.get('mobile_number', instance.mobile_number)
        instance.balance = validated_data.get('balance', instance.balance)
        instance.save()

        return instance
