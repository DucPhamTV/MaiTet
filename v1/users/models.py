from uuid import uuid4
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    GenderChoices = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('N', 'Don\'t Specify'),
    ]
    id = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    email = models.EmailField(verbose_name='email', unique=True,
                              blank=False, null=False, max_length=255)
    phone = models.CharField(null=True, max_length=50)
    avatar = models.URLField(blank=True, null=True)
    gender = models.CharField(
        max_length=1,
        choices=GenderChoices,
        null=True
    )
    REQUIRED_FIELDS = ['email', 'phone', 'avatar', 'gender']
    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"

    class Meta:
        ordering = ['username']
