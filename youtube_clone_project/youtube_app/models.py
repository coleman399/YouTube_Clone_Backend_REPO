from django.db import models

# Create your models here.
class Comments(models.Model):
    commentId = models.IntegerField(default=0, primary_key=True)
    parentId = models.IntegerField(default=0)
    body = models.CharField(max_length=300, default='', blank=True, null=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    
class BackendData(models.Model):
    videoId = models.CharField(max_length=25, primary_key=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    comments = models.ForeignKey(Comments, on_delete=models.CASCADE, blank=True, null=True)    