from django.db import models

class EmployeeRegister(models.Model):
    emp_id = models.IntegerField()
    emp_name = models.CharField(max_length= 23)
    emp_phone = models.IntegerField()
    emp_address = models.CharField(max_length=100)
    emp_email = models.EmailField()
    emp_salary = models.IntegerField()

    def __str__(self):
        return self.emp_name