from django.contrib.auth.models import User
from django.test.client import Client
import unittest,pytest
from django.urls import reverse
import collections


@pytest.mark.django_db
class LoginTestCase(unittest.TestCase):
    """
    This class is for unit testing. We will be testing our login feature

    """



    def setUp(self):

        """
        We will create a dummy user here.

        """

        self.client = Client()
        self.user = User.objects.create_user('john', 'john@gmail.com', 'johnpassword')

    def testLogin(self):

        """
        We will try to login by the dummy user and will see the response

        """

        self.client.login(username='john', password = 'johnpassword')
        response = self.client.get(reverse('user_login'))
        self.assertEqual(response.status_code, 200)