# Generated by Django 2.0.7 on 2018-08-02 18:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sitehighlight',
            old_name='article',
            new_name='highlights',
        ),
    ]