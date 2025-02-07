import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from api.models import Item

@pytest.mark.django_db
def test_create_item():
    client = APIClient()
    url = reverse("item-list-create")
    data = {"name": "Sample Item", "description": "This is a test item"}
    response = client.post(url, data, format="json")

    assert response.status_code == 201
    assert Item.objects.count() == 1
    assert Item.objects.first().name == "Sample Item"
