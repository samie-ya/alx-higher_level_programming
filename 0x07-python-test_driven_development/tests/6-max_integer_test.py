#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """This class is going to use the TestCase and check
       the function max_integer"""

    def test_order_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_integer(self):
        self.assertEqual(max_integer([3, 1, 9]), 9)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_ordered_negative_integer(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_unordered_negative_integer(self):
        self.assertEqual(max_integer([-98, -56, -2, 0]), 0)

    def test_one_content(self):
        self.assertEqual(max_integer([4]), 4)

    def test_ordered_float(self):
        self.assertEqual(max_integer([1.2, 2.3, 3.6, 4.4]), 4.4)

    def test_unordered_float(self):
        self.assertEqual(max_integer([1.34, 5.62, 8.93, 4.56]), 8.93)

    def test_unordered_negative_float(self):
        self.assertEqual(max_integer([-1.45, -34.2, -103, -0.4]), -0.4)

    def test_list(self):
        self.assertEqual(max_integer([[1, -2], [-3, 4]]), [1, -2])

    def test_list_similar(self):
        self.assertEqual(max_integer([[1, 2], [1, 2]]), [1, 2])

    def test_list_one_difference(self):
        self.assertEqual(max_integer([[1, 2], [1, -3]]), [1, 2])

    def test_list_large(self):
        self.assertEqual(max_integer([[1.89, -2.67, 83],
                         [-67.1, 0.2, 4.89], [91, -91.3], [5]]), [91, -91.3])

    def test_tuple(self):
        self.assertEqual(max_integer([(1, 2), (1, 2), (3, 4), (3, 4, 5)]),
                         (3, 4, 5))

    def test_letter(self):
        self.assertEqual(max_integer(["a", "b", "c", "d"]), "d")

    def test_words(self):
        self.assertEqual(max_integer(["Hello", "Apple", "Zebra", "hello",
                         "banana"]), "hello")

    def test_words_in_tuple(self):
        self.assertEqual(max_integer([("Hi, How are you?"),
                         ("I am fine, thank you"),
                         ("and, you?")]), ("and, you?"))

    def test_empty_tuple(self):
        self.assertEqual(max_integer([(), ()]), ())

    def test_empty_list_list(self):
        self.assertEqual(max_integer([[[]], [], [[[], []], []]]),
                         [[[], []], []])
