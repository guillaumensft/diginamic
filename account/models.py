from django.db import models

# Create your models here.

from django.contrib.auth.models import User


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='userprofile')
    point = models.PositiveIntegerField(default=10)
    bio = models.CharField(max_length=2000)
    first_name = models.CharField(max_length=500)
    last_name = models.CharField(max_length=500)


    def __str__(self):
        return str(self.user) or ""