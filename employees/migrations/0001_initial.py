# Generated by Django 4.1.7 on 2023-03-02 07:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resume', models.FileField(blank=True, null=True, upload_to='applications/resume')),
                ('expected_salary', models.CharField(choices=[('50k', '50k'), ('70k', '70k'), ('80k', '80k'), ('100k', '100k'), ('150k', '150k'), ('200k', '200k'), ('250k', '250k')], max_length=20)),
                ('summary', models.TextField(max_length=500)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=60)),
                ('project_description', models.TextField(max_length=500)),
                ('project_link', models.URLField(blank=True, null=True)),
                ('project_file', models.FileField(blank=True, null=True, upload_to='employee_project/project_file')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skills', models.CharField(choices=[('PY', 'Python'), ('DJ', 'Django'), ('FL', 'Flask'), ('JS', 'Javascript'), ('RT', 'Rust')], max_length=200)),
                ('education', models.CharField(choices=[('matric', 'Matric'), ('fsc-nm', 'Fsc_Non_Medical'), ('fsd-m', 'Fs.c_Medical'), ('bs-eng', 'Bachelor in English'), ('bscs', 'Bachelor in Computer Science'), ('bs-Math', 'Bachelor in Mathematics'), ('bs-IS', 'Bachelor in Islamist'), ('bba', 'Bachelor in Business'), ('bs_phy', 'Bachelor in Physics'), ('ms-eng', 'Masters in English'), ('ms-phy', 'Masters in Physics'), ('ms-math', 'Masters in Mathematics'), ('mscs', 'Master in Computer Science'), ('mphil', 'M-Phil'), ('phd-cs', 'P-hd in Computer science')], max_length=100)),
                ('about', models.TextField(max_length=500)),
                ('interest', models.CharField(choices=[('Teaching', 'Teaching'), ('Business', 'Business'), ('it', 'Information Technology'), ('cs', 'Computer Science'), ('cyber-s', 'Cyber Security'), ('ai', 'Artificial Intelligence'), ('mc', 'Machine Learning'), ('army', 'Army'), ('sports', 'Sports')], max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
