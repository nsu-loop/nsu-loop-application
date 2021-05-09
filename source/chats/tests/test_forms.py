import pytest
from django.urls import reverse

from chats.tests.test_views import TestChatBase


@pytest.fixture(autouse=True)
def enable_db_access(db):
 
    pass


class TestChatForm(TestChatBase):
   
    @pytest.fixture()
    def auth_client(self, from_user):
       
        from django.test.client import Client

        client = Client()
        client.force_login(from_user)
        return client

    @pytest.fixture
    def chat_url(self, to_user):
       
        return reverse("chats:chat-view", args=[to_user.id])

    def test_chat_create(self, from_user, auth_client, chat_url, to_user):
       
        assert from_user
        assert to_user

        data = {
            'to_user_id': to_user.id,
            'message': "Test message",
        }
        response = auth_client.post(
            chat_url,
            data=data,
            format='json'
        )
        assert response.status_code == 200

    def test_chat_list(self, from_user, auth_client, chat_url, to_user):
        
        assert from_user
        assert to_user

        response = auth_client.get(
            chat_url
        )
        assert response.status_code == 200
