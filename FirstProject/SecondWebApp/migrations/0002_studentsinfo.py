# Generated by Django 5.0.1 on 2024-01-22 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SecondWebApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentsInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('std_id', models.IntegerField()),
                ('std_name', models.CharField(max_length=20)),
                ('std_age', models.IntegerField()),
                ('std_contact', models.IntegerField()),
                ('std_email', models.EmailField(max_length=254)),
                ('std_course', models.CharField(max_length=20)),
            ],
        ),
    ]
