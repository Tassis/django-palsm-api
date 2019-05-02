"""
Plasm project tools kit.
"""
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.settings import api_settings

class JWTokenKit():
    """
    Adapter JWTAuthentication
    """
    backend = JWTAuthentication()
    def authenticate(self, request):
        """
        An authentication plugin that authenticates requests through a JSON web
        token provided in a request header.

        :param request: A HttpRequest.
        :returns return A User Object tuple.
        """
        return self.backend.authenticate(request)

    def get_user_id(self, request):
        """
        An Authenticates reuqests through Json Web Token provided in a request header
        :param request: A HttpRequest.
        :returns return A user_id.
        """
        header = self.backend.get_header(request)
        if header is None:
            return None

        raw_token = self.backend.get_raw_token(header)
        if raw_token is None:
            return None

        validated_token = self.backend.get_validated_token(raw_token)
        return validated_token[api_settings.USER_ID_CLAIM]
