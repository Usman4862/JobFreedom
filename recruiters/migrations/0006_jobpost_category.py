# Generated by Django 4.1.7 on 2023-03-16 08:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recruiters', '0005_jobcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobpost',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='recruiters.jobcategory'),
            preserve_default=False,
        ),
    ]