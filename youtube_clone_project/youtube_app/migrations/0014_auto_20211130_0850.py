# Generated by Django 3.2.9 on 2021-11-30 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtube_app', '0013_auto_20211129_0127'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='backenddata',
            name='comments',
        ),
        migrations.AddField(
            model_name='backenddata',
            name='comments',
            field=models.ManyToManyField(to='youtube_app.Comments'),
        ),
    ]
