from rest_framework import generics
from rest_framework.permissions import AllowAny
from users.models import Employee
from . import serializers


class RetrieveEmployee(generics.RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer
    lookup_field = 'card_id'
    permission_classes = [AllowAny]


class TopUpBalance(generics.UpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = serializers.TopUpSerializer
    lookup_field = 'id'
