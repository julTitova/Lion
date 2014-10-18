from unittest import TestCase
from Lion import Leo
import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        b = Leo('Tree')
        self.assertEqual('Tree', b.Object_view, "This is incorrect result")
        Leo.Hungry(b)
        Leo.Full(b)
        c = Leo('')
        self.assertEqual('', c.Object_view, "This is incorrect result")
        Leo.Hungry(c)
        Leo.Full(c)
        d = Leo(10)
        self.assertEqual(10, d.Object_view, "This is incorrect result")
        Leo.Hungry(d)
        Leo.Full(d)
        e = Leo('k')
        self.assertEqual('k', e.Object_view, "This is incorrect result")
        Leo.Hungry(e)
        Leo.Full(e)
if __name__ == '__main__':
    unittest.main()
