# Generated by Django 4.2.2 on 2023-08-19 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('JobsApp', '0003_alter_job_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='Address',
        ),
        migrations.RemoveField(
            model_name='job',
            name='Phone',
        ),
        migrations.RemoveField(
            model_name='job',
            name='Web',
        ),
    ]
