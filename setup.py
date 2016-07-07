# -*- coding: utf-8 -*-
"""Installer for the atreal.trello package."""

from setuptools import find_packages
from setuptools import setup

import os


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

long_description = \
    read('README.rst') + \
    read('docs', 'CHANGELOG.rst') + \
    read('docs', 'LICENSE.rst')

setup(
    name='atreal.trello',
    version='0.1',
    description="Trello integration fro atReal for dev.atreal.fr",
    long_description=long_description,
    # Get more from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
    ],
    keywords='trello atReal',
    author='atReal',
    author_email='contact@atreal.fr',
    url='http://pypi.python.org/pypi/atreal.trello',
    license='BSD',
    packages=find_packages('src', exclude=['ez_setup']),
    namespace_packages=['atreal'],
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Plone',
        'setuptools',
        'z3c.jbot',
    ],
    extras_require={
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
