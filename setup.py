"""
setup.py for python-orderby, following PyPA style
"""
from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='orderby',
    version='0.0.1',
    description='Python key functions for multi-field ordering',
    long_description=long_description,
    url='https://github.com/jvtm/python-orderby',
    author='Jyrki Muukkonen',
    author_email='jvtm@kruu.org',
    license='Apache 2.0',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='sort order orderby development',
    packages=find_packages(exclude=['tests']),
)
