# Generated by Django 3.2.9 on 2021-12-01 05:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('youtube_app', '0015_rename_comments_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='backenddata',
            name='comments',
        ),
        migrations.AddField(
            model_name='backenddata',
            name='comments',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='youtube_app.comment'),
        ),
    ]
