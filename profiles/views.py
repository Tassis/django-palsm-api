"""
Profiles view.
"""
from django.http import Http404
from rest_framework import permissions
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from plasmkit.utils import JWTokenKit

from .models import Profile
from .serializers import ProfileSerializer
# Create your views here.
JWT_AUTHEN = JWTokenKit()

class ProfilesList(APIView):
    """
    Profiles View
    """
    permission_classes = (permissions.IsAuthenticated,)
    def get(self, request, _format=None):
        """
        Get profiles list from token data.
        """
        # authentication user and get data.
        user = JWT_AUTHEN.authenticate(request)[0]
        profiles = Profile.objects.filter(**{'user_id_id': user.id})
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data, None)

    def post(self, request, _format=None):
        """
        Add new Profile to List.
        """
        user = JWT_AUTHEN.authenticate(request)[0]
        profile_name = request.data['profile_name']
        obj = Profile.objects.create(user_id=user, profile_name=profile_name)
        serializer = ProfileSerializer(obj)
        return Response(serializer.data)

class ProfilesDetail(APIView):
    """
    Profile's detail data view.
    """
    permission_classes = (permissions.IsAuthenticated,)
    def get_object(self, user, key):
        """
        get profile object by index.
        """
        try:
            return Profile.objects.get(user_id=user, profile_id=key)
        except:
            raise Http404

    def get(self, request, key, _format=None):
        """
        get profile data.
        """
        user = JWT_AUTHEN.authenticate(request)[0]
        obj = self.get_object(user, key)
        serializer = ProfileSerializer(obj)
        return Response(serializer.data)

    def put(self, request, key, _fomrat=None):
        """
        update profiles setting.
        """
        new_profile_name = request.data['profile_name']
        user = JWT_AUTHEN.authenticate(request)[0]
        obj = self.get_object(user, key)
        obj.profile_name = new_profile_name
        obj.save()
        return Response('put data success.', status=status.HTTP_200_OK)


    def delete(self, request, key, _format=None):
        """
        delete profile by key
        """
        user = JWT_AUTHEN.authenticate(request)[0]
        obj = self.get_object(user, key)
        obj.delete()
        return Response('delete profile success.', status=status.HTTP_202_ACCEPTED)