from django.http import HttpResponse
from django.urls import path
import djp

urlpatterns = [
    path("", lambda request: HttpResponse("Hello world"))
] + djp.urlpatterns()
