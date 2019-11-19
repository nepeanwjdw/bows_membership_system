from django.db import models
from django.contrib.auth.models import AbstractUser


class Employee(AbstractUser):
    id = models.IntegerField(primary_key=True, unique=True)
    card_id = models.CharField(max_length=16, unique=True)
    balance = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    mobile_number = models.CharField(max_length=30)
    username = None

    USERNAME_FIELD = 'id'
    REQUIRED_FIELDS = ['card_id']

    def __str__(self):
        """Returns the user's full name."""
        return '%s %s' % (self.first_name, self.last_name)

    def balance(self):
        """Returns the user's balance"""
        return self.balance
