# Generated by Django 3.2.9 on 2021-11-29 05:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('youtube_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='dislike',
            new_name='dislikes',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='like',
            new_name='likes',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='videoId',
            new_name='parentId',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='userComment',
        ),
        migrations.AddField(
            model_name='comment',
            name='body',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='comment',
            name='id',
            field=models.CharField(max_length=25, primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='BackendData',
            fields=[
                ('videoId', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('likes', models.IntegerField(default=0)),
                ('dislikes', models.IntegerField(default=0)),
                ('comments', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='youtube_app.comment')),
            ],
        ),
    ]
