from pluggy import HookimplMarker
from pluggy import HookspecMarker

hookspec = HookspecMarker("django_plugins")
hookimpl = HookimplMarker("django_plugins")


@hookspec
def installed_apps():
    """Return a list of Django app strings to be added to INSTALLED_APPS"""


@hookspec
def middleware():
    """
    Return a list of Django middleware class strings to be added to MIDDLEWARE.
    Optionally wrap with django_plugins.Before() or .After() to specify ordering
    """


@hookspec
def urlpatterns():
    """Return a list of url patterns to be added to urlpatterns"""


@hookspec
def settings(current_settings):
    """Modify current_settings in place to finish configuring settings.py"""
