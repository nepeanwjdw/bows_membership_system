from rest_framework import generics

from users import models
from . import serializers


class RetrieveEmployee(generics.RetrieveAPIView):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer
    lookup_field = 'card_id'
