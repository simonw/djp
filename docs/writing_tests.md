# Writing tests

The following projects include examples of tests written against a DJP plugin:

- [django-plugin-django-header](https://github.com/simonw/django-plugin-django-header) demonstrates [a simple test](https://github.com/simonw/django-plugin-django-header/blob/main/tests/test_django_plugin_django_header.py) that confirms that custom middleware is working by checking for anex expected HTTP header in the response.
- [django-plugin-blog](https://github.com/simonw/django-plugin-blog) has [tests](https://github.com/simonw/django-plugin-blog/blob/main/tests/test_django_plugin_blog.py) for a full application that includes custom models, views and templates.

Both of these projects follow the pattern described in [Using pytest-django with a reusable Django application](https://til.simonwillison.net/django/pytest-django).

## Running tests

If you created your plugin {ref}`using cookiecutter <cookiecutter>` you will have an initial test that you can run, and then extend.

To run the tests for your plugin it's best to create a dedicated virtual environment:
```bash
cd django-plugin-example
python -m venv venv
source venv/bin/activate
python -m pip install -e '.[test]'
python -m pytest
```
The output should look like this:
```
============================= test session starts ==============================
platform darwin -- Python 3.10.10, pytest-8.3.3, pluggy-1.5.0
django: version: 5.1.1, settings: tests.test_project.settings (from ini)
rootdir: /private/tmp/django-plugin-example
configfile: pyproject.toml
plugins: django-4.9.0
collected 1 item

tests/test_django_plugin_example.py .                                    [100%]

============================== 1 passed in 0.05s ===============================
```
