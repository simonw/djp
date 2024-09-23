# Writing tests

The following projects include examples of tests written against a DJP plugin:

- [django-plugin-django-header](https://github.com/simonw/django-plugin-django-header) demonstrates [a simple test](https://github.com/simonw/django-plugin-django-header/blob/main/tests/test_django_plugin_django_header.py) that confirms that custom middleware is working by checking for anex expected HTTP header in the response.
- [django-plugin-blog](https://github.com/simonw/django-plugin-blog) has [tests](https://github.com/simonw/django-plugin-blog/blob/main/tests/test_django_plugin_blog.py) for a full application that includes custom models, views and templates.

Both of these projects follow the pattern described in [Using pytest-django with a reusable Django application](https://til.simonwillison.net/django/pytest-django).