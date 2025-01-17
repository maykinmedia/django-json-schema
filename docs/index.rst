.. django-json-schema-model documentation master file, created by startproject.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to django-json-schema-model's documentation!
====================================================

|build-status| |code-quality| |black| |coverage|

..
   |docs| |python-versions| |django-versions| |pypi-version|

A reusable Django app to store JSON schemas.

Features
========

* JsonSchemaModel consisting of
    - name CharField
    - schema JsonField
    - validate(json) method to validate JSON against the schema.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   quickstart



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


.. |build-status| image:: https://github.com/maykinmedia/django-json-schema-model/workflows/Run%20CI/badge.svg
    :alt: Build status
    :target: https://github.com/maykinmedia/django-json-schema-model/actions?query=workflow%3A%22Run+CI%22

.. |code-quality| image:: https://github.com/maykinmedia/django-json-schema-model/workflows/Code%20quality%20checks/badge.svg
     :alt: Code quality checks
     :target: https://github.com/maykinmedia/django-json-schema-model/actions?query=workflow%3A%22Code+quality+checks%22

.. |black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black

.. |coverage| image:: https://codecov.io/gh/maykinmedia/django-json-schema-model/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/maykinmedia/django-json-schema-model
    :alt: Coverage status

..
   .. |docs| image:: https://readthedocs.org/projects/django-json-schema-model/badge/?version=latest
       :target: https://django-json-schema-model.readthedocs.io/en/latest/?badge=latest
       :alt: Documentation Status

   .. |python-versions| image:: https://img.shields.io/pypi/pyversions/django-json-schema-model.svg

   .. |django-versions| image:: https://img.shields.io/pypi/djversions/django-json-schema-model.svg

   .. |pypi-version| image:: https://img.shields.io/pypi/v/django-json-schema-model.svg
       :target: https://pypi.org/project/django-json-schema-model/
