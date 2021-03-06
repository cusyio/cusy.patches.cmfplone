# -*- coding: utf-8 -*-
"""Installer for the cusy.patches.cmfplone package."""

from setuptools import find_packages
from setuptools import setup


long_description = "\n\n".join(
    [
        open("README.rst").read(),
        open("CONTRIBUTORS.rst").read(),
        open("CHANGES.rst").read(),
    ]
)


setup(
    name="cusy.patches.cmfplone",
    version="1.0.0.dev0",
    description="Patches and fixes for Products.CMFPlone which are not yet released.",
    long_description=long_description,
    # Get more from https://pypi.org/classifiers/
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: Addon",
        "Framework :: Plone :: 5.2",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords="Python Plone CMS",
    author="Thomas Massmann",
    author_email="thomas.massmann@it-spir.it",
    url="https://github.com/cusyio/cusy.patches.cmfplone",
    project_urls={
        "PyPI": "https://pypi.python.org/pypi/cusy.patches.cmfplone",
        "Source": "https://github.com/cusyio/cusy.patches.cmfplone",
        "Tracker": "https://github.com/cusyio/cusy.patches.cmfplone/issues",
        # 'Documentation': 'https://cusy.patches.cmfplone.readthedocs.io/en/latest/',
    },
    license="GPL version 2",
    packages=find_packages("src", exclude=["ez_setup"]),
    namespace_packages=["cusy", "cusy.patches"],
    package_dir={"": "src"},
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.6",
    install_requires=[
        "setuptools",
        "collective.monkeypatcher",
        "Products.CMFPlone",
    ],
    extras_require={
        "test": [
            "plone.app.testing",
            # Plone KGS does not use this version, because it would break
            # Remove if your package shall be part of coredev.
            # plone_coredev tests as of 2016-04-01.
            "plone.testing>=5.0.0",
            "plone.app.contenttypes",
            "plone.app.robotframework[debug]",
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
