import pytest
from django import urls
from django.test.client import Client

@pytest.fixture
def payment_data():
    return {'mobile_number': '01737047772', 'transaction_id': '173772642'}    


@pytest.mark.django_db
def test_with_authenticated_client(client, django_user_model, jackpot_data):
    username = "Ahnaf"
    password = "1234"
    user = django_user_model.objects.create_user(username=username, password=password)
    client.login(username=username, password=password)
    make_url = "http://127.0.0.1:8000/payments/make/"
    confirm_url = "http://127.0.0.1:8000/payments/confirm/"
    response = client.post(make_url, data=payment_data)
    response = client.get(confirm_url)
    assert response.status_code == 200   