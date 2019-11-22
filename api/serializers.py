from rest_framework import serializers
from users.models import Employee
from transactions.models import Transaction
from rest_auth.serializers import LoginSerializer


class EmployeeNameSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'first_name', 'last_name')
        model = Employee
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = Employee(**validated_data)
        user.set_password(password)
        user.save()
        Employee.objects.create(user=user)

        return user


class TopUpSerializer(serializers.ModelSerializer):
    amount = serializers.DecimalField(write_only=True, max_digits=5, decimal_places=2)
    transaction_details = serializers.SerializerMethodField('top_up_amount')
    user_details = serializers.SerializerMethodField('get_user_details')

    def top_up_amount(self, instance):
        transaction = Transaction.objects.filter(user_id=instance).order_by('-date_time')[:1].values(
            'id', 'card_id', 'type', 'amount', 'date_time')[0]
        return transaction

    def get_user_details(self, instance):
        user_details = {
            "id": instance.id,
            "first_name": instance.first_name,
            "last_name": instance.last_name,
            "balance": instance.balance,
        }
        return user_details

    class Meta:
        fields = ('amount', 'user_details', 'transaction_details')
        model = Employee

    def update(self, instance, validated_data):
        amount = validated_data.get('amount', instance.balance)
        instance.top_up(amount)
        instance.save()
        Transaction.objects.create(user_id=instance, card_id=instance.card_id, type="TU", amount=amount)
        return instance


class CustomLoginSerializer(LoginSerializer):
    username = serializers.IntegerField(required=True, allow_null=False)
    email = None

    class Meta:
        model = Employee
