from unittest import TestCase
from Lion import Leo
import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        b = Leo('Tree')
        c = Leo('')
        d = Leo('k')
        e = Leo(10)
        Leo.Hungry(b)
        Leo.Hungry(c)
        Leo.Hungry(d)
        Leo.Hungry(e)

if __name__ == '__main__':
    unittest.main()
