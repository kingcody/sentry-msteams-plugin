#!/usr/bin/env python

from setuptools import setup, find_packages
import os

cwd = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
readme_text = open(os.path.join(cwd, 'README.md')).read()

setup(
    name='sentry-msteams-plugin',
    version='0.1.0',
    author='Cody Mize',
    url='https://github.com/kingcody/sentry-msteams-plugin',
    long_description=readme_text,
    long_description_content_type='text/markdown',
    licence='GPLv2',
    description='Sentry plugin for sending events to Microsoft Teams',
    packages=find_packages(),
    install_requires=[
        'sentry'
    ],
    include_package_data=True,
    entry_points={
        'sentry.apps': [
            'msteams = msteams',
        ],
        'sentry.plugins': [
            'msteams = msteams.plugin:TeamsPlugin',
        ]
    },
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ]
)
