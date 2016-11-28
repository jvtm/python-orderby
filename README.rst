orderby
=======

Python key functions for multi-field ordering in SQL ORDER BY fashion

.. image:: https://img.shields.io/pypi/v/orderby.svg
    :target: https://pypi.python.org/pypi/orderby

Meant to be used with built-in ``sorted()`` *key function*.

Supports also ``list.sort()`` doing *in-place sorting*.

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


In-place sorting of a list:

.. code-block:: python

    >>> files.sort(key=desc('path'))
    >>> print(json.dumps(files, indent=2))
    [
      {
        "size": 1234,
        "path": "foo/bar.txt"
      },
      {
        "size": 1234,
        "path": "foo/abc.bin"
      },
      {
        "size": 0,
        "path": "/dev/null"
      }
    ]
    >>> files.sort(key=desc('size').asc('path'))
    >>> print(json.dumps(files, indent=2))
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


Works also with `SortedContainers <http://www.grantjenks.com/docs/sortedcontainers/>`_:

.. code-block:: python

    >>> from sortedcontainers import SortedList
    >>> from orderby import desc
    >>> mylist = SortedList(key=desc('value'))
    >>> mylist
    SortedListWithKey([], key=<orderby.sorter.OrderBy object at 0x108f65978>, load=1000)
    >>> mylist.add({'value': 13})
    >>> mylist.add({'value': 2})
    >>> mylist.add({'value': 1000})
    >>> mylist
    SortedListWithKey([{'value': 1000}, {'value': 13}, {'value': 2}], key=<orderby.sorter.OrderBy object at 0x108f65978>, load=1000)


Internals
---------

To be explained here later...

