from django.db import models


class Transaction(models.Model):
    TOP_UP = 'TU'
    PURCHASE = 'PU'
    TYPE_CHOICES = [
        (TOP_UP, 'Top up'),
        (PURCHASE, 'Purchase food or drink'),
    ]

    user_id = models.ForeignKey('users.Employee', on_delete=models.CASCADE)
    card_id = models.CharField(max_length=16)
    type = models.CharField(max_length=2, choices=TYPE_CHOICES)
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Returns the transaction amount"""
        return '%s' % self.id
