from django.db import models

# Create your models here.
class SampleTable(models.Model):
    sam_id = models.IntegerField()
    name = models.CharField(max_length= 20)

    def __str__(self):
        return self.name

class StudentsInfo(models.Model):
    std_id = models.IntegerField()
    std_name = models.CharField(max_length= 20)
    std_age = models.IntegerField()
    std_contact = models.IntegerField()
    std_email = models.EmailField()
    std_course = models.CharField(max_length=20)

    def __str__(self):
        return self.std_name