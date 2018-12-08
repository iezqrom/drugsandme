# Generated by Django 2.1 on 2018-11-30 11:15

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0059_auto_20181017_0830'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlepage',
            name='blurb_en',
            field=wagtail.core.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name='articlepage',
            name='blurb_es',
            field=wagtail.core.fields.RichTextField(blank=True),
        ),
    ]