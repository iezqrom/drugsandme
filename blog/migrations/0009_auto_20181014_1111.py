# Generated by Django 2.0.9 on 2018-10-14 11:11

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_remove_mention_article_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mention',
            name='author',
            field=wagtail.core.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='mention',
            name='organisation_name',
            field=wagtail.core.fields.RichTextField(),
        ),
    ]
