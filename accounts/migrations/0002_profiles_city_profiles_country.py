# Generated by Django 4.2.2 on 2023-08-23 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profiles',
            name='City',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='profiles',
            name='Country',
            field=models.CharField(max_length=255, null=True),
        ),
    ]