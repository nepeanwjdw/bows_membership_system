from rest_framework import serializers
from users import models


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'card_id',
            'first_name',
            'last_name',
        )
        model = models.Employee
