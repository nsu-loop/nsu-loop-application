from django.contrib.auth.models import User
from django.test.client import Client
import unittest,pytest
from django.urls import reverse
import collections


@pytest.mark.django_db
class LoginTestCase(unittest.TestCase):
   
    """
    This class is for our unit testing. It will test our login feature.
    """



    def setUp(self):

        #It will create a dummy user first
        self.client = Client()
        self.user = User.objects.create_user('john', 'john@gmail.com', 'johnpassword')

    def testLogin(self):

        
        #It will try to login with the dummy user
        self.client.login(username='john', password = 'johnpassword')
        response = self.client.get(reverse('user_login'))
        self.assertEqual(response.status_code, 200)