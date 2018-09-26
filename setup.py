# -*- coding: utf-8 -*-
from __future__ import with_statement

from setuptools import setup, find_packages


requires = [
    'Sphinx >= 1.5',
    'six',
]


def readme():
    try:
        with open('README.rst') as f:
            return f.read()
    except IOError:
        pass


setup(
    name='nodela',
    version='0.0.1',
    url='https://github.com/xiaomingfuckeasylife/nodela',
    license='BSD',
    author='Hong Minhee',
    author_email='huangxiaoming@elastos.org',
    description='elastos blockchain entry port',
    long_description=readme(),
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Documentation',
        'Topic :: Utilities',
    ],
    platforms='any',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
)
