#!/usr/bin/env python

from setuptools import setup

setup(
    name='steamweb',
    version='0.1',
    description='lib to access/use steam web pages (stuff not exposed via API)',
    author='Jayme',
    author_email='tuxnet@gmail.com',
    url='https://github.com/jayme-github/steamweb',
    packages=['steamweb'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    scripts=['demo.py'],
)