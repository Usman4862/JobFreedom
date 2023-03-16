# Generated by Django 4.1.7 on 2023-03-16 08:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recruiters', '0007_alter_jobcategory_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobpost',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='jobs', to='recruiters.jobcategory'),
        ),
    ]