from pluggy import HookimplMarker
from pluggy import HookspecMarker

hookspec = HookspecMarker("djp")
hookimpl = HookimplMarker("djp")


@hookspec
def installed_apps():
    """Return a list of Django app strings to be added to INSTALLED_APPS"""


@hookspec
def middleware():
    """
    Return a list of Django middleware class strings to be added to MIDDLEWARE.
    Optionally wrap with djp.Before() or djp.After() to specify ordering,
    or wrap with djp.Position(name, before=other_name) to insert before another
    or djp.Position(name, after=other_name) to insert after another.
    """


@hookspec
def urlpatterns():
    """Return a list of url patterns to be added to urlpatterns"""


@hookspec
def settings(current_settings):
    """Modify current_settings in place to finish configuring settings.py"""
