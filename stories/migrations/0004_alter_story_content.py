# Generated by Django 3.2.6 on 2021-08-26 09:34

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0003_alter_story_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
