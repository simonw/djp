# DJP: Django Plugins

A plugin system for Django, based on [Pluggy](https://pluggy.readthedocs.io/).

See [DJP: A plugin system for Django](https://simonwillison.net/2024/Sep/25/djp-a-plugin-system-for-django/) for an introduction to this project.

## Why plugins?

Django has long promoted the idea of [reusable apps](https://docs.djangoproject.com/en/5.1/intro/reusable-apps/), and there is a thriving ecosystem of open source extensions to the framework.

Many of these require the user to manually configure them, by modifying their `settings.py` to add new strings to `INSTALLED_APPS` or `MIDDLEWARE`, or by adding new entries to their URL configuration.

DJP addresses this limitation: you can configure DJP once for a project, after which any DJP-compliant plugins you install will be able to automatically modify your Django configuration to enable their functionality.

## Available plugins

[django-plugin-django-header](https://github.com/simonw/django-plugin-django-header) is an example plugin that adds a `Django-Composition` HTTP header to every HTTP response containing the name of a random composition by Django Reinhardt.

[django-plugin-blog](https://github.com/simonw/django-plugin-blog) implements a full blog application for Django, with entries and tags and an Atom feed and a configured Django admin interface. Installing this plugin adds the blog under the `/blog/` URL path.

[django-plugin-database-url](https://github.com/simonw/django-plugin-database-url) configures Django to connect to the database defined by the `DATABASE_URL` environment variable.

[django-plugin-datasette](https://github.com/simonw/django-plugin-datasette) adds a [Datasette](https://datasette.io) instance to Django, providing a read-only UI and JSON API for exploring data in any SQLite databases configured using Django’s `DATABASES` setting.

## Documentation

```{toctree}
---
maxdepth: 3
---
installing_plugins
creating_a_plugin
writing_tests
plugin_hooks
```
