from nose.tools import assert_equal
from parameterized import parameterized, parameterized_class
import unittest
from sample.FizzBuzz import *

class FizzBuzzParTests(unittest.TestCase):

    def setUp(self):
        self.tmp = FizzBuzz()

    @parameterized.expand([
        (5, "Buzz"),
        (-20, "Buzz"),
        (46731460, "Buzz"),
        (3, "Fizz"),
        (-9, "Fizz"),
        (-102, "Fizz"),
        (15, "FizzBuzz"),
        (7, "7"),
        (-13, "-13")
    ])

    def test_pos(self, number, expected):
        self.assertEqual(self.tmp.game(number), expected)

    @parameterized.expand([
        ("trzy",),
        ((),),
        ([],),
        ({},),
        (2.5,),
        (True,),
        (None,)
    ])

    def test_exc(self, e):
        self.assertRaises(Exception, self.tmp.game, e)

@parameterized_class(('number', 'expected'), [
    (5, "Buzz"),
    (-20, "Buzz"),
    (46731460, "Buzz"),
    (3, "Fizz"),
    (-9, "Fizz"),
    (-102, "Fizz"),
    (15, "FizzBuzz"),
    (7, "7"),
    (-13, "-13")
])

class FizzBuzzParTests2(unittest.TestCase):
    def setUp(self):
        self.tmp = FizzBuzz()

    def test_sec_pos(self):
        self.assertEqual(self.tmp.game(self.number), self.expected)

@parameterized_class(('e'), [
    ("trzy",),
    ((),),
    ([],),
    ({},),
    (2.5,),
    (True,),
    (None,)
])

class FizzBuzzParTests3(unittest.TestCase):
    def setUp(self):
        self.tmp = FizzBuzz()

    def test_exc_sec(self):
        self.assertRaises(Exception, self.tmp.game, self.e)

if __name__ == '__main__':
    unittest.main()