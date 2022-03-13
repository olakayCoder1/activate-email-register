from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    bio = models.TextField()
    address = models.TextField()
    is_verified = models.BooleanField(default=False)

class AccountAcivation(models.Model):
    user_mail = models.EmailField()
    active_token = models.CharField(max_length=150)
