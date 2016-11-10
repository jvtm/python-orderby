orderby
=======

Python key functions for multi-field ordering in SQL ORDER BY fashion

.. image:: https://img.shields.io/pypi/v/orderby.svg
    :target: https://pypi.python.org/pypi/orderby

Meant to be used with built-in ``sorted()`` *key function*.

Implementation uses ``operator.itemgetter()`` + some internal helper classes to allow descending sorting order.

So far this is tested and used on *lists of dictionaries*. Adding support for named tuples and others would
be possible (using ``operator.attrgetter()``).


Usage
-----

- SQL-like: ``orderby('foo ASC, bar DESC')``
- chained: ``asc('foo').desc('bar')`` usage
- multiple fields at once: ``asc('foo', 'bar')``


Examples
--------

``orderby()`` string syntax:

.. code-block:: python

    >>> from orderby import orderby
    >>> import json
    >>> files = [
    ...   {'size': 1234, 'path': 'foo/bar.txt'},
    ...   {'size': 0, 'path': '/dev/null'},
    ...   {'size': 1234, 'path': 'foo/abc.bin'},
    ... ]
    >>> print(json.dumps(sorted(files, key=orderby('size DESC, path')), indent=2))
    [
      {
        "size": 1234,
        "path": "foo/abc.bin"
      },
      {
        "size": 1234,
        "path": "foo/bar.txt"
      },
      {
        "size": 0,
        "path": "/dev/null"
      }
    ]


Chained `asc()` and `desc()` usage:

.. code-block:: python

    >>> from orderby import asc, desc
    >>> print(json.dumps(sorted(files, key=desc('size').asc('path')), indent=2))
    [
      {
        "size": 1234,
        "path": "foo/abc.bin"
      },
      {
        "size": 1234,
        "path": "foo/bar.txt"
      },
      {
        "size": 0,
        "path": "/dev/null"
      }
    ]


Internals
---------

To be explained here later...
