from django.db import models
from django.db import models
from cloudinary.models import CloudinaryField  
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    profile_picture = CloudinaryField('pictures/',default='http://res.cloudinary.com/dim8pysls/image/upload/v1639001486/x3mgnqmbi73lten4ewzv.png')
    bio = models.TextField(max_length=500, default="My Bio", blank=True)
    name = models.CharField(max_length=250, blank=True)
  

    def __str__(self):
        return f'{self.user.username} Profile'
