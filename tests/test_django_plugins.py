from django.conf import settings
from django.test.client import Client


def test_middleware_order():
    assert settings.MIDDLEWARE == [
        "tests.test_project.middleware.MiddlewareBefore",
        "tests.test_project.middleware.Middleware",
        "tests.test_project.middleware.Middleware4",
        "tests.test_project.middleware.Middleware2",
        "tests.test_project.middleware.Middleware5",
        "tests.test_project.middleware.Middleware3",
        "tests.test_project.middleware.MiddlewareAfter",
    ]


def test_middleware():
    response = Client().get("/")
    assert response["X-DJP-Middleware-After"] == "MiddlewareAfter"
    assert response["X-DJP-Middleware"] == "Middleware"
    assert response["X-DJP-Middleware-Before"] == "MiddlewareBefore"
    request = response._request
    assert hasattr(request, "_notes")
    assert request._notes == [
        "MiddlewareAfter",
        "Middleware3",
        "Middleware5",
        "Middleware2",
        "Middleware4",
        "Middleware",
        "MiddlewareBefore",
    ]


def test_urlpatterns():
    response = Client().get("/from-plugin/")
    assert response.content == b"Hello from a plugin"


def test_settings():
    assert settings.FROM_PLUGIN == "x"


def test_installed_apps():
    assert "tests.test_project.app1" in settings.INSTALLED_APPS
