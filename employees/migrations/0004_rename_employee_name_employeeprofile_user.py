# Generated by Django 4.1.7 on 2023-03-15 20:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0003_rename_user_employeeprofile_employee_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employeeprofile',
            old_name='employee_name',
            new_name='user',
        ),
    ]
