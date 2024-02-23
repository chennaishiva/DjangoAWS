from django.contrib import admin

from .models import SampleTable, StudentsInfo

# Register your models here.

admin.site.register(SampleTable)

admin.site.register(StudentsInfo)