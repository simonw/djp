# Creating a plugin

A Plugin is a Python package, usually named with `django-plugin-` as a prefix.

(cookiecutter)=

## Using cookiecutter

You can use the [simonw/django-plugin](https://github.com/simonw/django-plugin) to create an initial skeleton for your plugin, including automated tests, continuous integration and publishing to PyPI using GitHub Actions.

Install [cookiecutter](https://github.com/cookiecutter/cookiecutter):

```bash
pipx install cookiecutter # or pip install
```
Then run the template like this:
```bash
cookiecutter gh:simonw/django-plugin
```
The template will ask you a number of questions. Here's an example run:

```
  [1/6] plugin_name (): django-plugin-example
  [2/6] description (): A simple example plugin
  [3/6] hyphenated (django-plugin-example):
  [4/6] underscored (django_plugin_example):
  [5/6] github_username (): simonw
  [6/6] author_name (): Simon Willison
```
This creates a directory called `django-plugin-example` containing the skeleton of the plugin:

```
django-plugin-example
django-plugin-example/django_plugin_example
django-plugin-example/django_plugin_example/__init__.py
django-plugin-example/LICENSE
django-plugin-example/pyproject.toml
django-plugin-example/tests
django-plugin-example/tests/test_django_plugin_example.py
django-plugin-example/tests/test_project
django-plugin-example/tests/test_project/__init__.py
django-plugin-example/tests/test_project/settings.py
django-plugin-example/tests/test_project/urls.py
django-plugin-example/__init__.py
django-plugin-example/README.md
django-plugin-example/.gitignore
django-plugin-example/.github
django-plugin-example/.github/workflows
django-plugin-example/.github/workflows/publish.yml
django-plugin-example/.github/workflows/test.yml
```

## Creating a plugin without the template

Your plugin should have a `pyproject.toml` file that defines it, looking something like this:

### pyproject.toml

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

### Plugin directory structure

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
pip install -e path/to/django-plugin-example
```
