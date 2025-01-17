

Welcome to django-json-schema-model's documentation!
====================================================

:Version: 0.1.0
:Source: https://github.com/maykinmedia/django-json-schema-model
:Keywords: ``<keywords>``
:PythonVersion: 3.10

|build-status| |code-quality| |black| |coverage| |docs|

|python-versions| |django-versions| |pypi-version|

A reusable Django app to store JSON schemas.

.. contents::

.. section-numbering::

Features
========

* JsonSchemaModel consisting of
    - name CharField
    - schema JsonField
    - validate(json) method to validate JSON against the schema.

Installation
============

Requirements
------------

* Python 3.10 or above
* Django 4.2 or newer
* A database supporting django.db.models.JSONField


Install
-------

.. code-block:: bash

    pip install django-json-schema-model


Usage
=====

.. code-block:: python

    from django_json_schema_model.models import JsonSchema

    class ProductType(models.Model):
        schema = models.ForeignKey(JsonSchema, on_delete=models.PROTECT)

    class Product(models.Model):
        json = models.JsonField()
        type = models.ForeignKey(ProductType, on_delete=models.CASCADE)

        def clean(self):
            self.type.schema.validate(self.json)

Local development
=================

To install and develop the library locally, use::

.. code-block:: bash

    pip install -e .[tests,coverage,docs,release]

When running management commands via ``django-admin``, make sure to add the root
directory to the python path (or use ``python -m django <command>``):

.. code-block:: bash

    export PYTHONPATH=. DJANGO_SETTINGS_MODULE=testapp.settings
    django-admin check
    # or other commands like:
    # django-admin makemessages -l nl


.. |build-status| image:: https://github.com/maykinmedia/django-json-schema-model/workflows/Run%20CI/badge.svg
    :alt: Build status
    :target: https://github.com/maykinmedia/django-json-schema-model/actions?query=workflow%3A%22Run+CI%22

.. |code-quality| image:: https://github.com/maykinmedia/django-json-schema-model/workflows/Code%20quality%20checks/badge.svg
     :alt: Code quality checks
     :target: https://github.com/maykinmedia/django-json-schema-model/actions?query=workflow%3A%22Code+quality+checks%22

.. |black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black

.. |coverage| image:: https://codecov.io/gh/maykinmedia/django-json-schema-model/branch/main/graph/badge.svg
    :target: https://codecov.io/gh/maykinmedia/django-json-schema-model
    :alt: Coverage status

.. |docs| image:: https://readthedocs.org/projects/django-json-schema-model/badge/?version=latest
    :target: https://django-json-schema-model.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. |python-versions| image:: https://img.shields.io/pypi/pyversions/django-json-schema-model.svg

.. |django-versions| image:: https://img.shields.io/pypi/djversions/django-json-schema-model.svg

.. |pypi-version| image:: https://img.shields.io/pypi/v/django-json-schema-model.svg
    :target: https://pypi.org/project/django-json-schema-model/
