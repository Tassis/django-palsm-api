"""
Profiles Serializers.
"""
from rest_framework import serializers

from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    """
    All Profile List Serializer.
    """
    class Meta:
        model = Profile
        fields = '__all__'
