# DJP: Django Plugins

[![PyPI](https://img.shields.io/pypi/v/djp.svg)](https://pypi.org/project/djp/)
[![Tests](https://github.com/simonw/djp/actions/workflows/test.yml/badge.svg)](https://github.com/simonw/djp/actions/workflows/test.yml)
[![Changelog](https://img.shields.io/github/v/release/simonw/djp?include_prereleases&label=changelog)](https://github.com/simonw/djp/releases)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/simonw/djp/blob/main/LICENSE)

A plugin system for Django

## Installation

Install this library using `pip`:
```bash
pip install djp
```

## Configuration

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

## Usage

Installing a plugin in the same environment as your Django application should cause that plugin to automatically add the necessary 

## Development

To contribute to this library, first checkout the code. Then create a new virtual environment:
```bash
cd djp
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
