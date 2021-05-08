import pytest
from django import urls
from django.test.client import Client
from django.urls import reverse

@pytest.mark.parametrize('param', [
    ('home-view')
])

def test_render_views(client, param):
    temp_url = urls.reverse(param)
    resp = client.get(temp_url)
    assert resp.status_code == 200


@pytest.mark.django_db
def test_with_authenticated_client(client, django_user_model, jackpot_data):
    username = "simon"
    password = "123"
    user = django_user_model.objects.create_user(username=username, password=password)
    client.login(username=username, password=password)
    make_url = "http://127.0.0.1:8000/jackpots/make/"
    confirm_url = "http://127.0.0.1:8000/jackpots/confirm/"
    response = client.post(make_url, data=jackpot_data)
    response = client.get(confirm_url)
    assert response.status_code == 200    