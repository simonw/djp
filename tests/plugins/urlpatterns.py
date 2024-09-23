from django.urls import path
from django.http import HttpResponse
import djp


@djp.hookimpl
def urlpatterns():
    return [path("from-plugin/", lambda request: HttpResponse("Hello from a plugin"))]
