from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=10, null=True)
    nickname = models.CharField(null=True, max_length=10)
    email = models.EmailField(null=True)
    def __str__(self):
        return str(self.user)