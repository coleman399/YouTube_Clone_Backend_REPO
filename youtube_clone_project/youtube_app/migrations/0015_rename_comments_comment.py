# Generated by Django 3.2.9 on 2021-12-01 05:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('youtube_app', '0014_auto_20211130_0850'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comments',
            new_name='Comment',
        ),
    ]