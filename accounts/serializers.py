"""
Accounts's Serializers
"""
from rest_framework import serializers

from .models import Account

class AccountSerializer(serializers.ModelSerializer):
    """
    AccountSerializer data.
    """
    class Meta:
        model = Account
        fields = ('id', 'username', 'profile_count')
