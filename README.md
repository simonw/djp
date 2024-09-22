# django-plugins

[![PyPI](https://img.shields.io/pypi/v/django-plugins.svg)](https://pypi.org/project/django-plugins/)
[![Tests](https://github.com/simonw/django-plugins/actions/workflows/test.yml/badge.svg)](https://github.com/simonw/django-plugins/actions/workflows/test.yml)
[![Changelog](https://img.shields.io/github/v/release/simonw/django-plugins?include_prereleases&label=changelog)](https://github.com/simonw/django-plugins/releases)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/simonw/django-plugins/blob/main/LICENSE)

A plugin system for Django

## Installation

Install this library using `pip`:
```bash
pip install django-plugins
```

## Configuration

Add this to your `settings.py` file:
```python
import django_plugins

# ...

INSTALLED_APPS = [
    "your_app1",
    "your_app2",
] + django_plugins.installed_apps()

# ...

MIDDLEWARE = django_plugins.middleware([
    "your_middleware1",
    "your_middleware2",
])

# And at the very end of that file:
django_plugins.settings(globals())
```
And add this to your URL configuration in `urls.py`:
```python
urlpatterns = [
    # ...
] + django_plugins.urlpatterns()
```

## Usage

Installing a plugin in the same environment as your Django application should cause that plugin to automatically add the necessary 

## Development

To contribute to this library, first checkout the code. Then create a new virtual environment:
```bash
cd django-plugins
python -m venv venv
source venv/bin/activate
```
Now install the dependencies and test dependencies:
```bash
python -m pip install -e '.[test]'
```
To run the tests:
```bash
python -m pytest
```
