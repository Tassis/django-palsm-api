"""
Comment test file.
"""
from django.test import TestCase
from rest_framework.test import APIClient

# Create your tests here.
class CommentsTestCase(TestCase):
    """
    Comments Test case
    """
    data = {
        'username' : "dingo",
        'password' : "dingodingo22",
        'email' : "dingo@dingo.com"
    }
    client = None

    def setUp(self):
        """
        Test case setup
        """
        # create accounts.
        self.client = APIClient()
        response = self.client.post('/accounts/register/', {
            'username': self.data['username'],
            'password1': self.data['password'],
            'password2': self.data['password'],
            'email': self.data['email']
        })
        # login account.
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.login())
        assert response.status_code >= 200 and response.status_code < 300
        # create profile
        self.client.post('/profiles/', {'profile_name': 'jarijari1'})
        # create test page
        self.client.post('/pages/', {
            'profile_id': 1,
            'page_id': 1,
            'title': 'Testpage',
            'url': 'http://localhost:8000/testpage/',
            'identifier': '/testpage'
        })
        return

    def test_comment_post(self):
        """
        Test add comment.
        """
        response = self.create_comment('yee', 'yee@yee.com')
        self.assertTrue(response.data['username'] == 'yee')

    def test_comment_get(self):
        """
        Test get post list.
        """
        self.create_comment('yee', 'yee@yee.com')
        self.create_comment('yee1', 'yee1@yee.com')
        self.create_comment('yee2', 'yee2@yee.com')
        response = self.client.get('/comments/')
        self.assertTrue(len(response.data) == 3)

    def create_comment(self, name, email):
        """
        create comment.
        """
        response = self.client.post('/comments/', {
            'profile_id': 1,
            'page_id': 1,
            'username': name,
            'email': email,
            'content': 'test contnet'
        })
        return response

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
