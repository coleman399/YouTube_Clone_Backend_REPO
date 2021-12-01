from rest_framework import serializers
from .models import BackendData, Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['commentId', 'parentId', 'body', 'likes', 'dislikes']   
class BackendSerializer(serializers.ModelSerializer):
    class Meta:
        model = BackendData
        fields = ['videoId', 'likes', 'dislikes', 'comments']
        
        comments = CommentSerializer()
        
        depth= 1
    
    def create(self, validated_data):
        comments_data = validated_data.pop('comments')
        comment_model = Comment.objects.create(**comments_data)  
        backendData = BackendData.objects.create(comments=comment_model, **validated_data) 
        return backendData

    # def update(self, instance, validated_data):
    #     comment_data = validated_data.pop('comments')
    #     # Unless the application properly enforces that this field is
    #     # always set, the following could raise a `DoesNotExist`, which
    #     # would need to be handled.
    #     comments = instance.comments

    #     instance.commentId = validated_data.get('commentId', instance.commentId)
    #     instance.parentId = validated_data.get('parentId', instance.parentId)
    #     instance.body = validated_data.get('body', instance.body)
    #     instance.likes = validated_data.get('likes', instance.likes)
    #     instance.dislikes = validated_data.get('dislikes', instance.dislikes)
    #     instance.save()

    #     comments.save()

    #     return instance