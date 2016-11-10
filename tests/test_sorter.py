"""
Low-level unit tests for orderby.sorter internal helpers and classes
"""
from orderby.sorter import Desc, OrderBy
from unittest import TestCase


class TestDesc(TestCase):
    """ Tests for Desc helper class """
    def test_desc_simple(self):
        a = Desc('a')
        a2 = Desc('a')
        b = Desc('b')
        self.assertGreater(a, b)
        self.assertGreaterEqual(a, a)
        self.assertLess(b, a)
        self.assertLessEqual(b, a)
        self.assertEqual(a, a2)
        self.assertEqual(sorted([a, b, a, a]), [b, a, a, a])


class TestOrderBy(TestCase):
    """ Tests for OrderBy helper class """
    def test_orderby_chain_as_key_function(self):
        items = [
            {'a': 3, 'b': 0, 'c': True},
            {'a': 1, 'b': 0, 'c': False},
            {'a': 2, 'b': -1, 'c': True},
            {'a': 2, 'b': 42, 'c': False},
            {'a': 2, 'b': 1, 'c': False},
        ]
        for item in items:
            sortkey = OrderBy().asc('a').asc('b')(item)
            self.assertEqual(sortkey, (item['a'], item['b']))
