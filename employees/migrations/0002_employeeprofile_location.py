# Generated by Django 4.1.7 on 2023-03-15 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeeprofile',
            name='location',
            field=models.CharField(default='Pakistan', max_length=30),
        ),
    ]
