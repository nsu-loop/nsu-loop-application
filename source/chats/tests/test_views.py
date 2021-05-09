import random

import pytest
from django.contrib.auth.models import User

from chats.models import Chat


@pytest.fixture(autouse=True)
def enable_db_access(db):
   
    pass


class TestChatBase:
   

    @pytest.fixture
    def from_user(self, ):
       
        username = f"user{random.randint(9, 99999)}"
        return User.objects.create(
            username=username
        )

    @pytest.fixture
    def to_user(self, ):
        
        username = f"user{random.randint(9, 99999) + 1}"
        return User.objects.create(
            username=username
        )

    @pytest.fixture
    def chat(self, from_user, to_user):
       

        return Chat.objects.create(
            from_user=from_user,
            to_user=to_user,
            message="this is a test message."
        )


class TestChatList(TestChatBase):
   

    def test_empty_chat_list(self, from_user, to_user):
        
        assert not Chat.objects.filter(
            id=from_user.id
        )

        assert not Chat.objects.filter(
            to_user=to_user.id
        )

    def test_chat_list(self, chat):
        
        assert chat
        assert Chat.objects.filter(
            id=chat.from_user.id
        )
        assert Chat.objects.filter(
            to_user=chat.to_user.id
        )
