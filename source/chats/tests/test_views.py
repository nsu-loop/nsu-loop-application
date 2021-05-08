import random

import pytest
from django.contrib.auth.models import User

from chats.models import Chat


@pytest.fixture(autouse=True)
def enable_db_access(db):
    """
    Global DB access to all tests.
    :param db:
    :return:
    """
    pass


class TestChatBase:
    """
    This class contains all the required fixtures for the Chat test suit
    """

    @pytest.fixture
    def from_user(self, ):
        """
        creates a test user
        :return: the object of the test user
        """
        username = f"user{random.randint(9, 99999)}"
        return User.objects.create(
            username=username
        )

    @pytest.fixture
    def to_user(self, ):
        """
        creates a test user
        :return: the object of the test user
        """
        username = f"user{random.randint(9, 99999) + 1}"
        return User.objects.create(
            username=username
        )

    @pytest.fixture
    def chat(self, from_user, to_user):
        """
        creates a chat entry in the database
        :param from_user: the sender person of the chat
        :param to_user: the receiver person of the chat
        :return: the chat object
        """

        return Chat.objects.create(
            from_user=from_user,
            to_user=to_user,
            message="this is a test message."
        )


class TestChatList(TestChatBase):
    """
    Inside this class, all the test cases related to chat will be tested.
    """

    def test_empty_chat_list(self, from_user, to_user):
        """
        Testing the empty chat list's behaviour
        :param from_user: the sender user
        :param to_user: the receiver user
        :return:
        """
        assert not Chat.objects.filter(
            id=from_user.id
        )

        assert not Chat.objects.filter(
            to_user=to_user.id
        )

    def test_chat_list(self, chat):
        """
        Testing the populated chat list's behaviour
        :param chat: the chat object of both from_user and to_user
        :return:
        """
        assert chat
        assert Chat.objects.filter(
            id=chat.from_user.id
        )
        assert Chat.objects.filter(
            to_user=chat.to_user.id
        )
