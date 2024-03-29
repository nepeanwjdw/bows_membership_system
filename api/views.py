from rest_framework import generics
from rest_framework.permissions import AllowAny
from users.models import Employee
from . import serializers


class RetrieveEmployeeView(generics.RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = serializers.EmployeeNameSerializer
    lookup_field = 'card_id'
    permission_classes = [AllowAny]


class RegisterEmployeeView(generics.CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = serializers.EmployeeRegisterSerializer
    permission_classes = [AllowAny]


class TopUpView(generics.UpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = serializers.TopUpSerializer
    lookup_field = 'id'


class EmployeeDetailsView(generics.RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = serializers.EmployeeDetailsSerializer
    lookup_field = 'id'
