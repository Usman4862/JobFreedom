# Generated by Django 4.1.7 on 2023-03-01 08:51

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
            name='Recruiter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_job_post', models.CharField(blank=True, max_length=50, null=True)),
                ('skills', models.CharField(choices=[('Py', 'Python'), ('React', 'React'), ('DJ', 'Django'), ('FLASK', 'Flask'), ('HTML', 'Html'), ('CSS', 'CSS')], max_length=10)),
                ('education', models.CharField(choices=[('matric', 'Matric'), ('inter', 'Intermediate'), ('BS', 'BSCS'), ('Master-in-Math', 'Master in Math'), ('S-Engineering', 'Sofware Engineering')], max_length=30)),
                ('about', models.TextField(blank=True, max_length=50, null=True)),
                ('total_employees_hired', models.PositiveIntegerField()),
                ('company_name', models.CharField(max_length=15)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Recruiter')),
            ],
        ),
    ]