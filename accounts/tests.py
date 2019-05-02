"""
Accounts test file.
"""
from django.test import TestCase
from rest_framework.test import APIClient
import json

class AccountsTestCase(TestCase):
    """
    Accounts TestCase.
    """
    data = {
        'username' : "dingo",
        'password' : "dingodingo22",
        'email' : "dingo@dingo.com"
    }
    client = None

    def setUp(self):
        """
        initialize and register account test.
        """
        self.client = APIClient()
        response = self.client.post('/accounts/register/', {
            'username': self.data['username'],
            'password1': self.data['password'],
            'password2': self.data['password'],
            'email': self.data['email']
        })

        print("StatusCode:", response.status_code)
        self.assertTrue(response.status_code >= 200 and
                        response.status_code <= 300, 'yeeee')

    def test_account_login(self):
        """
        login account test.
        """
        token = self.login()
        self.assertIsInstance(token, str)
        
    def test_account_getdata(self):
        """
        login account get data test.
        """
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.login())
        response = self.client.get('/accounts/detail/')
        self.assertTrue(response.status_code >= 200 and response.status_code < 300)
        print(response.json())

    def login(self):
        """
        login method.
        """
        response = self.client.post('/token/', {
            'username': self.data['username'],
            'password': self.data['password'],
            'email': self.data['email']
        })
        return response.json()['access']
