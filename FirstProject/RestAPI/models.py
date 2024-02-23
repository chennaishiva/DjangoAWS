from django.db import models

class userRegister(models.Model):
    username = models.CharField(max_length= 20)
    email = models.EmailField()
    address = models.CharField(max_length=50)
    password = models.CharField(max_length=20)

