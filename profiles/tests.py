"""
Profiles test file.
"""
from django.test import TestCase
from rest_framework.test import APIClient

# Create your tests here.
class ProfilesTestCase(TestCase):
    """
    Profile API TestCase
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
        self.client = APIClient()
        response = self.client.post('/accounts/register/', {
            'username': self.data['username'],
            'password1': self.data['password'],
            'password2': self.data['password'],
            'email': self.data['email']
        })
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.login())
        assert response.status_code >= 200 and response.status_code < 300
        return

    def test_profiles_post(self):
        """
        Test add new profile.
        """
        response = self.client.post('/profiles/', {
            'profile_name':'dingo'
        })
        self.assertTrue(response.data['user_id'] == 1)

    def test_profiles_get(self):
        """
        profiles get.
        """
        response = self.client.post('/profiles/', {'profile_name':'dingo1'})
        response = self.client.post('/profiles/', {'profile_name':'dingo2'})
        response = self.client.post('/profiles/', {'profile_name':'dingo3'})
        response = self.client.get('/profiles/')
        self.assertTrue(len(response.data) == 3)
        self.assertTrue(response.data[0]['user_id'] == 1)

    def test_profile_detail_get(self):
        """
        Test get profile detail.
        """
        response = self.client.post('/profiles/', {'profile_name':'dingo1'})
        response = self.client.post('/profiles/', {'profile_name':'dingo2'})
        response = self.client.post('/profiles/', {'profile_name':'dingo3'})
        response = self.client.get('/profiles/1/')
        print(response.data)
        self.assertTrue(response.data['user_id'] == 1)
        return

    def test_profile_detail_put(self):
        """
        Test update profile data.
        """
        self.client.post('/profiles/', {'profile_name':'dingo1'})
        response = self.client.put('/profiles/1/',{'profile_name':'dingo2'})
        self.assertTrue(response.status_code == 200)

    def test_profile_detail_delete(self):
        """
        Test delete profile
        """
        self.client.post('/profiles/', {'profile_name':'dingo1'})
        self.client.post('/profiles/', {'profile_name':'dingo2'})
        self.client.post('/profiles/', {'profile_name':'dingo3'})
        response = self.client.delete('/profiles/1/')
        self.assertEqual(response.status_code, 202)
        return

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
