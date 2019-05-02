from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Account
from .serializers import AccountSerializer


JWTAuthen = JWTAuthentication()

class AccountDetail(APIView):
    """
    Show account data.
    
    must login.
    """
    permission_classes = (permissions.IsAuthenticated,)
    def get(self, request, format=None):
        user = JWTAuthen.authenticate(request)[0]
        serializer = AccountSerializer(user)
        return Response(serializer.data)    