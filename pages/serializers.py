"""
Pages Serializers file.
"""
from rest_framework import serializers

from .models import Page

class PageSerializers(serializers.ModelSerializer):
    """
    All Page serializers
    """
    class Meta:
        model = Page
        fields = '__all__'

    