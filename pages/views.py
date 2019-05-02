"""
Pages View file.
"""
from rest_framework import generics

from .serializers import PageSerializers
from .models import Page

# Create your views here.
class PageView(generics.ListCreateAPIView):
    """
    page list operation.
    """
    queryset = Page.objects.all()
    serializer_class = PageSerializers


class PageDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    single page's operation.
    """
    queryset = Page.objects.all()
    serializer_class = PageSerializers
    