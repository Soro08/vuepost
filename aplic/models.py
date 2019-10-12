from django.db import models

# Create your models here.

class MyImage(models.Model):
    image = models.ImageField(upload_to='image')
    name = models.CharField(max_length = 255, null = True)
    username = models.CharField(max_length = 255, null = True)
    email = models.CharField(max_length = 255, null = True)
    phone = models.CharField(max_length = 255, null = True)
    