from django.test.client import Client


def test_django_plugins():
    response = Client().get("/")
    request = response._request
    assert hasattr(request, "_notes")
