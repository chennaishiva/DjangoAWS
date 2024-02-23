import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "FirstProject.settings")

django.setup()

from curdapp.models import EmployeeRegister
from faker import Faker
from random import *

faker = Faker()
def fakeemployeedata():
    f_id = randint(200, 999)
    f_name = faker.name()
    f_phone = randint(7000000000, 9000000000)
    f_address = faker.city()
    f_email = faker.email()
    f_salary = randint(20000, 50000)
    emp = EmployeeRegister.objects.get_or_create(emp_id = f_id,
                                                 emp_name = f_name,
                                                 emp_phone = f_phone,
                                                 emp_address = f_address,
                                                 emp_email = f_email,
                                                 emp_salary = f_salary,
                                                 )

for i in range(11):
    fakeemployeedata()