# Plugin Hooks

The following plugin hooks can be used by plugins.

## installed_apps()

Return a list of Django app strings to be added to `INSTALLED_APPS`.

Example implementation:

```python
import djp

@djp.hookimpl
def installed_apps():
    return ["my_plugin_app"]
```

## middleware()

Return a list of Django middleware class strings to be added to MIDDLEWARE.

Middleware can optionally be wrapped with `djp.Before()` or `djp.After()` to specify ordering relative to existing middleware.

Example implementation:

```python
import djp

@djp.hookimpl
def middleware():
    return [
        djp.Before("django.middleware.common.CommonMiddleware"),
        "my_plugin.middleware.MyPluginMiddleware",
        djp.After("django.middleware.clickjacking.XFrameOptionsMiddleware")
    ]
```

## urlpatterns()

Return a list of URL patterns to be added to `urlpatterns`.

Example implementation:

```python
import djp
from django.urls import path
from . import views

@djp.hookimpl
def urlpatterns():
    return [
        path("my-plugin/", views.my_plugin_view),
    ]
```

## settings(current_settings)

Modify the current Django settings in-place to configure additional settings.

`current_settings` is a dictionary representing the current settings in `settings.py`.

Example implementation:

```python
import djp

@djp.hookimpl
def settings(current_settings):
    current_settings["DATABASES"] = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": "mydatabase",
        }
    }
```
