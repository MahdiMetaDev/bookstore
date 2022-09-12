from email.policy import default
from django.db import models
from django.contrib.auth import get_user_model


class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)

    avatar = models.ImageField(default='default.png', upload_to='profile_images/')
    bio = models.TextField()

    def __str__(self):
        return self.user.username
