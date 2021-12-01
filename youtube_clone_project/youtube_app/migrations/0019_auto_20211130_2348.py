# Generated by Django 3.2.9 on 2021-12-01 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtube_app', '0018_rename_videoid_comment_backenddata'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='backendData',
        ),
        migrations.AddField(
            model_name='backenddata',
            name='comments',
            field=models.ManyToManyField(to='youtube_app.Comment'),
        ),
    ]