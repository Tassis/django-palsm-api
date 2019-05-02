"""
pages test file.
"""
from django.test import TestCase
from rest_framework.test import APIClient
# Create your tests here.
class PagesTestCase(TestCase):
    """
    Pages app testcase.
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
        return

    def test_pages_post(self):
        """
        Test create page.
        """
        title = 'Joooooriiiiii'
        url = 'http://localhost:8000/tassis/yee'
        identifier = '/tassis/yee/'
        response = self.create_page(title, url, identifier)
        self.assertTrue(response.data['page_id'] == 1)
        return

    def test_pages_get(self):
        """
        Test create page.
        """
        # create page.
        title = 'Joooooriiiiii'
        url = 'http://localhost:8000/tassis/yee'
        identifier = '/tassis/yee/'
        self.create_page(title, url, identifier)
        self.create_page(f'{title}1', f'{url}1', f'{url}1')
        self.create_page(f'{title}2', f'{url}2', f'{url}2')
        self.create_page(f'{title}3', f'{url}3', f'{url}3')
        # get pages.
        response = self.client.get('/pages/')
        self.assertTrue(len(response.data) > 1)

    def test_page_detial_put(self):
        """
        Test Page put
        """
       # create page.
        title = 'Joooooriiiiii'
        url = 'http://localhost:8000/tassis/yee'
        identifier = '/tassis/yee/'
        self.create_page(title, url, identifier)
        self.create_page(f'{title}1', f'{url}1', f'{url}1')
        self.create_page(f'{title}2', f'{url}2', f'{url}2')
        self.create_page(f'{title}3', f'{url}3', f'{url}3')
        # put page
        response = self.client.put('/pages/1/', {
            'url' : url,
            'title' : title,
            'identifier': identifier
        })
        self.assertTrue(response.data['title'] == title)

    def test_page_detial_patch(self):
        """
        Test page patch operation.
        """
       # create page.
        title = 'Joooooriiiiii'
        url = 'http://localhost:8000/tassis/yee'
        identifier = '/tassis/yee/'
        self.create_page(title, url, identifier)
        self.create_page(f'{title}1', f'{url}1', f'{url}1')
        self.create_page(f'{title}2', f'{url}2', f'{url}2')
        self.create_page(f'{title}3', f'{url}3', f'{url}3')
        # patch page detail.
        response = self.client.patch('/pages/1/', {
            'url': 'http://localhost:8999'
        })
        print(response.data)

    def create_page(self, title, url, identifier):
        """
        Create test page.
        """
        profile_id = 1
        response = self.client.post('/pages/',
                                     {
                                         'profile_id': profile_id,
                                         'title': title,
                                         'url': url,
                                         'identifier': identifier
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
