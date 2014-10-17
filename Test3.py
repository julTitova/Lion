from unittest import TestCase
from Lion import Leo
import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        b = Leo('Tree')
        c = Leo('')
        d = Leo('k')
        self.assertEqual('Tree', b.Object_view, "This is incorrect result")
        self.assertEqual('', c.Object_view, "This is incorrect result")
        self.assertEqual('k', d.Object_view, "This is incorrect result")
if __name__ == '__main__':
    unittest.main()
