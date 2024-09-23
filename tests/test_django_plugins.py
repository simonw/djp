from django.test.client import Client


def test_middleware():
    response = Client().get("/")
    assert response["X-DJP-Middleware-After"] == "MiddlewareAfter"
    assert response["X-DJP-Middleware"] == "Middleware"
    assert response["X-DJP-Middleware-Before"] == "MiddlewareBefore"
    request = response._request
    assert hasattr(request, "_notes")
    assert request._notes == ["MiddlewareAfter", "Middleware", "MiddlewareBefore"]


def test_urlpatterns():
    response = Client().get("/from-plugin/")
    assert response.content == b"Hello from a plugin"
