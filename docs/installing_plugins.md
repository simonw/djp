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

Try this example plugin, which adds a custom HTTP header with a line from the Zen of Python:

```bash
pip install django-zen-of-python
```

Now run `curl` against your application to see the new header:

```bash
curl -I http://localhost:8000/
```
