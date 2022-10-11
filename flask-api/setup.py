"""Python package config."""

from setuptools import setup

setup(
    name='course493',
    version='0.1.0',
    packages=['course493'],
    include_package_data=True,
    install_requires=[
        'Flask',
        'requests',
    ],
    python_requires='>=3.6',
)
