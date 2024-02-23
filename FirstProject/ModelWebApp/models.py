from django.db import models

# Create your models here.

class Trainers(models.Model):
    trainer_id = models.IntegerField()
    trainer_name = models.CharField(max_length= 20)
    trainer_age = models.IntegerField()

