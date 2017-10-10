#!/usr/bin/env python

import os
import sys

from setuptools import setup, find_packages


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

readme = open('README.rst').read()
doclink = """
Documentation
-------------

The full documentation is at http://instar.rtfd.org."""
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='instar',
    version='0.1.0',
    description='Synthesizabe soft core modules for FPGA',
    long_description=readme + '\n\n' + doclink + '\n\n' + history,
    author='Euripedes Rocha Filho',
    author_email='rocha.euripedes@gmail.com',
    url='https://github.com/euripedesrocha/instar',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    package_dir={'instar': 'instar'},
    include_package_data=True,
    dependency_links=['https://github.com/jandecaluwe/myhdl/archive/master.tar.gz'],
    install_requires=[],
    tests_require=['pytest'],
    license='MIT',
    zip_safe=False,
    keywords='instar',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
)
