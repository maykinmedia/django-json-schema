==========
Quickstart
==========

Installation
============

Install from PyPI with pip:

.. code-block:: bash

    pip install django-json-schema-model


Usage
=====

.. code-block:: python

    from django.db import models
    from django_json_schema_model.models import JsonSchema

    class ProductType(models.Model):
        schema = models.ForeignKey(JsonSchema, on_delete=models.PROTECT)

    class Product(models.Model):
        json = models.JsonField()
        type = models.ForeignKey(ProductType, on_delete=models.CASCADE)

        def clean(self):
            self.type.schema.validate(self.json)
