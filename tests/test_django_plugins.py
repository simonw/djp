from django.test.client import Client


def test_django_plugins():
    response = Client().get("/")
    assert response["X-DJP-Middleware-After"] == "MiddlewareAfter"
    assert response["X-DJP-Middleware"] == "Middleware"
    assert response["X-DJP-Middleware-Before"] == "MiddlewareBefore"
    request = response._request
    assert hasattr(request, "_notes")
    assert request._notes == ["MiddlewareAfter", "Middleware", "MiddlewareBefore"]
