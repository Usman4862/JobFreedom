# Generated by Django 4.1.7 on 2023-03-16 09:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recruiters', '0008_alter_jobpost_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='recruiter',
            name='company_name',
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='recruiters.country')),
            ],
        ),
        migrations.AddField(
            model_name='recruiter',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='recruiters.company'),
        ),
    ]
