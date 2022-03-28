from django.db import models
from django.utils.text import slugify
from django.utils.crypto import get_random_string

# Create your models here.

from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='userprofile')
    point = models.PositiveIntegerField(default=10)
    bio = models.CharField(max_length=2000)
    first_name = models.CharField(max_length=500)
    last_name = models.CharField(max_length=500)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return str(self.user) or ""

    def get_absolute_url(self):
        return Profile('account:profile-list', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if self.slug:
            super(Profile, self).save(*args, **kwargs)
        else:
            self.slug = slugify(str(self.user) + get_random_string(9))
            super(Profile, self).save(*args, **kwargs)

