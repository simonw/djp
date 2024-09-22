# Plugin Hooks

The following plugin hooks can be used by plugins.

## installed_apps()

Return a list of Django app strings to be added to `INSTALLED_APPS`.

Example implementation:

```python
@django_plugins.hookimpl
def installed_apps():
    return ["my_plugin_app"]
```

## middleware()

Returnsa list of Django middleware class strings to be added to MIDDLEWARE.

Middleware can optionally be wrapped with `django_plugins.Before()` or `django_plugins.After()` to specify ordering relative to existing middleware.

Example implementation:

```python
@django_plugins.hookimpl
def middleware():
    return [
        django_plugins.Before("django.middleware.common.CommonMiddleware"),
        "my_plugin.middleware.MyPluginMiddleware",
        django_plugins.After("django.middleware.clickjacking.XFrameOptionsMiddleware")
    ]
```

## urlpatterns()

Returns a list of URL patterns to be added to `urlpatterns`.

Example implementation:

```python
from django.urls import path
from . import views

@django_plugins.hookimpl
def urlpatterns():
    return [
        path("my-plugin/", views.my_plugin_view),
    ]
```

## settings(current_settings)

Allows modifying the current Django settings in-place to configure additional settings.

Example implementation:

```python
@django_plugins.hookimpl
def settings(current_settings):
    current_settings["DATABASES"] = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": "mydatabase",
        }
    }
```
