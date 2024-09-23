# Installing plugins

To install plugins that use this system you will first need to configure the plugin system in your Django application.

Install this library using `pip`:
```bash
pip install djp
```

## Modifying your configuration

Add this to your `settings.py` file:
```python
import djp

# ...

INSTALLED_APPS = [
    "your_app1",
    "your_app2",
] + djp.installed_apps()

# ...

MIDDLEWARE = djp.middleware([
    "your_middleware1",
    "your_middleware2",
])

# And at the very end of that file:
djp.settings(globals())
```
And add this to your URL configuration in `urls.py`:
```python
urlpatterns = [
    # ...
] + djp.urlpatterns()
```

## Adding plugins to your environment

You can now install plugins, using `pip` or your package manager of choice.

Try this example plugin, which adds a custom HTTP header with a random composition written by Django Reinhardt:

```bash
pip install django-plugin-django-header
```

Now run `curl` against your application to see the new header:

```bash
curl -I http://localhost:8000/
```

## Listing installed plugins

The `showplugins` management command lists the plugins that are installed in your current environment:

```bash
./manage.py showplugins
```
Example output:
```json
[
  {
    "name": "django-plugin-blog",
    "hooks": [
      "installed_apps",
      "middleware",
      "settings",
      "urlpatterns"
    ],
    "version": "0.1"
  },
  {
    "name": "django-plugin-django-header",
    "hooks": [
      "middleware"
    ],
    "version": "0.1"
  }
]
```

## Loading plugins from a directory

You can also set the `DJP_PLUGINS_DIR` environment variable to point to a directory which contains `*.py` files implementing plugins.

This can be useful for plugin development, and is also used by DJP's own automated tests.
