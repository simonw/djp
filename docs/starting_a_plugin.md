# Creating a plugin

A Plugin is a Python package. It should have a `pyproject.toml` file that defines it, looking something like this:

```toml
[project]
name = "django-plugin-special-header"
version = "0.1"
description = "Add a HTTP header to a Django app"
readme = "README.md"
authors = [{name = "Simon Willison"}]
license = {text = "Apache-2.0"}
classifiers = [
    "License :: OSI Approved :: Apache Software License"
]
dependencies = [
    "django",
    "djp",
]

[project.entry-points.djp]
django_plugin_special_header = "django_plugin_special_header"
```
The key part here is the `[project.entry-points.djp]` section. This tells the plugins system how to load the plugin - it should look for the `django_plugin_special_header` package or module.

Next, create the directory structure. For this plugin that will look like this:

```
django-plugin-special-header/
    django_plugin_special_header/
        __init__.py
        middleware.py
    pyproject.toml
    README.md
```
The `__init__.py` file should contain the plugin hook implementations. For this middleware example that will look like this:

```python
import djp


@djp.hookimpl
def middleware():
    return ["django_plugin_secial_header.middleware.SpecialHeaderMiddleware"]
```
The `middleware.py` file should contain the actual middleware implementation. Here's an example:

```python
class SpecialHeaderMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response["Special-Header"] = "This is a special HTTP header"
        return response
```

## Trying out the plugin

In local development you can add this plugin to your existing Django environment by running this command:

```bash
pip install -e path/to/django-plugin-special-header
```
