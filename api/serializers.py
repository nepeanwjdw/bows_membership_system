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


class TopUpSerializer(serializers.Serializer):
    amount = serializers.DecimalField(write_only=True, max_digits=5, decimal_places=2)

    class Meta:
        model = Employee

    def update(self, instance, validated_data):
        amount = validated_data.get('amount', instance.balance)
        instance.balance += amount
        instance.save()
        return instance
