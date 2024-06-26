from django.db import models # type: ignore
from django.conf import settings # type: ignore


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    photo = models.ImageField(upload_to='users/%y/%m/%d', blank=True)

    def __str__(self):
        return f'Profile for user {self.user.username}'
    
    