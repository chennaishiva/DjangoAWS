from django.db import models

class RegisterModels(models.Model):
    Firstname = models.CharField(max_length=20)
    Lastname = models.CharField(max_length=20)
    Email = models.EmailField()
    Password = models.CharField(max_length=12)
    Confirm_password = models.CharField(max_length=12)

    def __str__(self):
        return self.Firstname