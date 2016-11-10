"""
Unit-tests for orderby module public interface, in the way
it is supposed to be used in sorted() and others
"""
from orderby import asc, desc, orderby
from unittest import TestCase

TEST_DATA_PERSONS = (
    {'id': 0, 'lastname': 'Smith', 'firstname': 'John', 'age': 42, 'score': 50},
    {'id': 1, 'lastname': 'Smith', 'firstname': 'Jane', 'age': 37, 'score': 100},
    {'id': 2, 'lastname': 'A', 'firstname': 'B', 'age': 20, 'score': 50},
    {'id': 3, 'lastname': 'A', 'firstname': 'A', 'age': 20, 'score': 50},
)


def get_ids(items):
    """ id fields from sorted list-of-dicts """
    return tuple(x['id'] for x in items)


class TestOrderByAPI(TestCase):
    def test_asc_desc_chain(self):
        result = sorted(TEST_DATA_PERSONS, key=desc('age').asc('lastname', 'firstname').desc('score'))
        self.assertEqual(get_ids(result), (0, 1, 3, 2))

    def test_asc_inits_the_chain(self):
        keyf = asc('foo')
        self.assertTrue(callable(keyf.asc))
        self.assertTrue(callable(keyf.desc))

    def test_desc_inits_the_chain(self):
        keyf = desc('bar')
        self.assertTrue(callable(keyf.asc))
        self.assertTrue(callable(keyf.desc))

    def test_desc_same_as_reverse(self):
        rdesc = sorted(TEST_DATA_PERSONS, key=desc('lastname'))
        rrev = sorted(TEST_DATA_PERSONS, key=asc('lastname'), reverse=True)
        self.assertEqual(rdesc, rrev)

    def test_orderby_qstrings(self):
        expected = (
            # order by string -> expected id order
            ('lastname, firstname, score', (3, 2, 1, 0)),
            ('score DESC, age DESC, lastname, firstname', (1, 0, 3, 2)),
            ('id DESC', (3, 2, 1, 0)),
        )
        for qstring, result in expected:
            ordered = sorted(TEST_DATA_PERSONS, key=orderby(qstring))
            self.assertEqual(get_ids(ordered), result)

    def test_inplace_sorting(self):
        copied = list(TEST_DATA_PERSONS)
        self.assertEqual(get_ids(copied), (0, 1, 2, 3))
        copied.sort(key=orderby('score DESC, lastname, firstname, age, id'))
        self.assertEqual(get_ids(copied), (1, 3, 2, 0))
