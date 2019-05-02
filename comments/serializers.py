"""
Comment serializers file.
"""
from rest_framework import serializers

from .models import Comment

class CommentSerializers(serializers.ModelSerializer):
    """
    Comment field serializer
    """
    class Meta:
        model = Comment
        fields = '__all__'
