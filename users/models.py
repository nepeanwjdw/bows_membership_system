from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class Employee(AbstractUser):
    id = models.IntegerField(primary_key=True, unique=True)
    card_id = models.CharField(max_length=16, unique=True)
    email = models.EmailField()
    balance = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    mobile_number = models.CharField(max_length=30)
    username = None

    USERNAME_FIELD = 'id'
    REQUIRED_FIELDS = ['card_id', 'email']

    objects = UserManager()

    def __str__(self):
        """Returns the user's full name."""
        return '%s %s' % (self.first_name, self.last_name)

    def top_up(self, amount):
        self.balance += amount
        return self.balance
