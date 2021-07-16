.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on pypi or github. It is a comment.

.. image:: https://github.com/cusyio/cusy.patches.cmfplone/workflows/ci/badge.svg
    :target: https://github.com/cusyio/cusy.patches.cmfplone/actions
    :alt: CI Status

.. image:: https://codecov.io/gh/cusyio/cusy.patches.cmfplone/branch/main/graph/badge.svg?token=6ZIOKJ1BVX
    :target: https://codecov.io/gh/cusyio/cusy.patches.cmfplone
    :alt: Coverage Status

.. image:: https://img.shields.io/pypi/v/cusy.patches.cmfplone.svg
    :target: https://pypi.python.org/pypi/cusy.patches.cmfplone/
    :alt: Latest Version

.. image:: https://img.shields.io/pypi/status/cusy.patches.cmfplone.svg
    :target: https://pypi.python.org/pypi/cusy.patches.cmfplone
    :alt: Egg Status

.. image:: https://img.shields.io/pypi/pyversions/cusy.patches.cmfplone.svg?style=plastic   :alt: Supported - Python Versions

.. image:: https://img.shields.io/pypi/l/cusy.patches.cmfplone.svg
    :target: https://pypi.python.org/pypi/cusy.patches.cmfplone/
    :alt: License


=====================
cusy.patches.cmfplone
=====================

Patches and fixes for `Products.CMFPlone <https://github.com/plone/Products.CMFPlone/>`_ which are not yet released.

Patches
-------

- Plone Controlpanel should use expression context with Plone support:
  https://github.com/plone/Products.CMFPlone/issues/3288


Installation
------------

Install ``cusy.patches.cmfplone`` by adding it to your buildout::

    [buildout]

    ...

    eggs =
        cusy.patches.cmfplone


and then running ``bin/buildout``


Contribute
----------

- Issue Tracker: https://github.com/cusyio/cusy.patches.cmfplone/issues
- Source Code: https://github.com/cusyio/cusy.patches.cmfplone


Support
-------

If you are having issues, please let us know by adding a new ticket.


License
-------

The project is licensed under the GPLv2.
