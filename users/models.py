from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default_prod.jpeg', upload_to='profile_pics')
    phone_nuber = models.CharField(max_length=10, default='XXXXXXXXXX')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

        try:
            this = Profile.objects.get(id=self.id)
            if this.image != self.image:
                this.image.delete()
        except: pass