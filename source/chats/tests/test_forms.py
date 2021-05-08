import pytest
from django.urls import reverse

from chats.tests.test_views import TestChatBase


@pytest.fixture(autouse=True)
def enable_db_access(db):
    """
    Global DB access to all tests.
    :param db:
    :return:
    """
    pass


class TestChatForm(TestChatBase):
    """
    Inside this class, all the test cases related to chat forms will be tested.
    """

    @pytest.fixture()
    def auth_client(self, from_user):
        """A Django test client logged in as an admin user."""
        from django.test.client import Client

        client = Client()
        client.force_login(from_user)
        return client

    @pytest.fixture
    def chat_url(self, to_user):
        """
        preparing the url for the chat
        :param to_user: the receiver user
        :return: the url for the chat list and create
        """
        return reverse("chats:chat-view", args=[to_user.id])

    def test_chat_create(self, from_user, auth_client, chat_url, to_user):
        """
        Testing chat's behaviour with single user, trying to crete a new message
        :param from_user: the sender user
        :param to_user: the receiver user
        :param chat_url: the url for chats
        :param auth_client: http client for posting and getting data
        :return:
        """
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
        """
        Testing chat's behaviour with single user, trying the list of chats
        :param from_user: the sender user
        :param to_user: the receiver user
        :param chat_url: the url for chats
        :param auth_client: http client for posting and getting data
        :return:
        """
        assert from_user
        assert to_user

        response = auth_client.get(
            chat_url
        )
        assert response.status_code == 200
