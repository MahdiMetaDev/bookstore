from django.db import models
from django.contrib.auth import get_user_model
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)

    avatar = models.ImageField(default='default.png', upload_to='profile_images/')
    bio = models.TextField()

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.avatar.path)

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.avatar.path)
