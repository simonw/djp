# DJP: Django Plugins

A plugin system for Django, based on [Pluggy](https://pluggy.readthedocs.io/).

## Why plugins?

Django has long promoted the idea of [reusable apps](https://docs.djangoproject.com/en/5.1/intro/reusable-apps/), and there is a thriving ecosystem of open source extensions to the framework.

Many of these require the user to manually configure them, by modifying their `settings.py` to add new strings to `INSTALLED_APPS` or `MIDDLEWARE`, or by adding new entries to their URL configuration.

DJP addresses this limitation: you can configure DJP once for a project, after which any DJP-compliant plugins you install will be able to automatically modify your Django configuration to enable their functionality.

```{toctree}
---
maxdepth: 3
---
installing_plugins
creating_a_plugin
writing_tests
plugin_hooks
```
