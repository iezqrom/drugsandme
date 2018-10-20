# Generated by Django 2.0.7 on 2018-08-09 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0026_remove_highlight_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='highlight',
            old_name='link',
            new_name='link_en',
        ),
        migrations.AddField(
            model_name='highlight',
            name='link_es',
            field=models.CharField(default=models.CharField(max_length=255), max_length=255),
        ),
        migrations.AddField(
            model_name='highlight',
            name='name_en',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='highlight',
            name='name_es',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]