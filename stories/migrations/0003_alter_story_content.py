# Generated by Django 3.2.6 on 2021-08-26 08:13

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0002_story_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
