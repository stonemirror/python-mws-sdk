# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

version = '0.2'

REQUIREMENTS = ['requests']

CLASSIFIERS = [
    'Development Status :: 2 - Pre-Alpha',
    'Environment :: Web Environment',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development',
    'Topic :: Software Development :: Libraries :: Application Frameworks',
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 2.6",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3.4",
]

setup(
    name="amazon-mws",
    version=version,
    description="A python interface for Amazon MWS",
    author="Juozas Kaziukenas",
    author_email="juozas@juokaz.com",
    url="https://github.com/juokaz/python-amazon-mws",
    packages=find_packages(),
    platforms=['OS Independent'],
    license='LICENSE.txt',
    install_requires=REQUIREMENTS,
    classifiers=CLASSIFIERS,
    include_package_data=True,
    zip_safe=False
)
