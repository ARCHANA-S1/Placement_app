# Generated by Django 4.2.6 on 2023-12-20 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_jobs_job_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentprofile',
            name='saved_jobs',
            field=models.ManyToManyField(null=True, related_name='saved', to='myapp.jobs'),
        ),
    ]
