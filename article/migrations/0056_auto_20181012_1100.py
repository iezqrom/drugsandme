# Generated by Django 2.0.9 on 2018-10-12 11:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0055_auto_20181011_2133'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articlepage',
            name='slug_en',
        ),
        migrations.RemoveField(
            model_name='articlepage',
            name='slug_es',
        ),
    ]