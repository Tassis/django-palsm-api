"""
Comments view file.
"""
from rest_framework import generics

from .serializers import CommentSerializers
from .models import Comment
# Create your views here.
class CommentsView(generics.ListCreateAPIView):
    """
    Comments list view.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializers

class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Comment data view.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializers
