#!/usr/bin/python3
"""Unittest for the function and attribute in class Rectangle"""

from io import StringIO
import unittest
from unittest.mock import patch

from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """This class is going to use the TestCase and check
       the function and attribute in class rectangle"""

    def test_class(self):
        self.assertIs(type(Rectangle), type(Base))

    def test_public_id_3(self):
        b = Rectangle(1, 3, 5, 8, 9)
        self.assertEqual(b.id, 9)

    def test_no_arguments(self):
        with self.assertRaises(TypeError):
            b = Rectangle()

    def test_one_argument(self):
        with self.assertRaises(TypeError):
            b = Rectangle(1)

    def test_many_arguments(self):
        with self.assertRaises(TypeError):
            b = Rectangle(1, 2, 3, 4, 5, 6)

    def test_attributes(self):
        b = Rectangle(1, 2, 3, 4, 6)
        self.assertIs(b.width, 1)
        self.assertIs(b.height, 2)
        self.assertIs(b.x, 3)
        self.assertIs(b.y, 4)
        self.assertIs(b.id, 6)

    def test_attributes_2(self):
        b = Rectangle(2, 3)
        b.width = 10
        b.height = 5
        b.x = 10
        b.y = 6
        b.id = 5
        self.assertIs(b.width, 10)
        self.assertIs(b.height, 5)
        self.assertIs(b.x, 10)
        self.assertIs(b.y, 6)
        self.assertIs(b.id, 5)

    def test_area(self):
        b = Rectangle(2, 5)
        self.assertEqual(b.area(), 10)

    def test_area(self):
        b = Rectangle(3, 4, 5, 6)
        self.assertEqual(b.area(), 12)

    def test_area_with_argument(self):
        b = Rectangle(1, 4)
        with self.assertRaises(TypeError):
            b.area(1)

    def test_display(self):
        b = Rectangle(2, 3)
        on_screen = "##\n##\n##\n"
        with patch('sys.stdout', new=StringIO()) as f:
            b.display()
            self.assertEqual(f.getvalue(), on_screen)

    def test_display_2(self):
        b = Rectangle(4, 6)
        on_screen = "####\n####\n####\n####\n####\n####\n"
        with patch('sys.stdout', new=StringIO()) as f:
            b.display()
            self.assertEqual(f.getvalue(), on_screen)

    def test_display_with_x_and_y(self):
        b = Rectangle(2, 3, 4, 5, 7)
        on_screen = "\n\n\n\n\n    ##\n    ##\n    ##\n"
        with patch('sys.stdout', new=StringIO()) as f:
            b.display()
            self.assertEqual(f.getvalue(), on_screen)

    def test_display_with_argument(self):
        b = Rectangle(1, 2)
        with self.assertRaises(TypeError):
            b.display(3)

    def test_str_(self):
        b = Rectangle(2, 2, 2, 2, 2)
        self.assertEqual(str(b), "[Rectangle] (2) 2/2 - 2/2")

    def test_str_2(self):
        b = Rectangle(1, 2, 3, 4, 5)
        b1 = Rectangle(3, 4, 5, 6, 7)
        self.assertEqual(str(b1), "[Rectangle] (7) 5/6 - 3/4")

    def test_str_3(self):
        b = Rectangle(2, 4, 6, 8, 10)
        with self.assertRaises(TypeError):
            b.__str__(1)

    def test_update(self):
        b = Rectangle(10, 9, 8, 7, 6)
        b.update()
        self.assertEqual(str(b), "[Rectangle] (6) 8/7 - 10/9")
        b.update(89)
        self.assertEqual(str(b), "[Rectangle] (89) 8/7 - 10/9")
        b.update(89, 90)
        self.assertEqual(str(b), "[Rectangle] (89) 8/7 - 90/9")
        b.update(89, 90, 91)
        self.assertEqual(str(b), "[Rectangle] (89) 8/7 - 90/91")
        b.update(89, 90, 91, 92)
        self.assertEqual(str(b), "[Rectangle] (89) 92/7 - 90/91")
        b.update(89, 90, 91, 92, 93)
        self.assertEqual(str(b), "[Rectangle] (89) 92/93 - 90/91")

    def test_update_kwagrs(self):
        b = Rectangle(10, 9, 8, 7, 6)
        b.update()
        self.assertEqual(str(b), "[Rectangle] (6) 8/7 - 10/9")
        b.update(x=5)
        self.assertEqual(str(b), "[Rectangle] (6) 5/7 - 10/9")
        b.update(x=2, y=3)
        self.assertEqual(str(b), "[Rectangle] (6) 2/3 - 10/9")
        b.update(x=3, id=5, y=4)
        self.assertEqual(str(b), "[Rectangle] (5) 3/4 - 10/9")
        b.update(x=4, height=5, y=6, id=7)
        self.assertEqual(str(b), "[Rectangle] (7) 4/6 - 10/5")
        b.update(height=3, x=4, width=5, y=6, id=7)
        self.assertEqual(str(b), "[Rectangle] (7) 4/6 - 5/3")

    def test_to_dictionary(self):
        b = Rectangle(10, 9, 8, 7, 6)
        b1 = b.to_dictionary()
        self.assertEqual(b1, {'id': 6, 'width': 10, 'height': 9,
                         'x': 8, 'y': 7})

    def test_to_dictionary_2(self):
        b = Rectangle(1, 1, 1, 1, 1)
        b1 = b.to_dictionary()
        self.assertEqual(b1, {'id': 1, 'width': 1, 'height': 1,
                         'x': 1, 'y': 1})

    def test_to_dictionary_3(self):
        b = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaises(TypeError):
            b.to_dictionary(3)


class TestErrorInTypesForWidth(unittest.TestCase):
    """This class is going to use the TestCase and check
       diffrent datatypes and the error they create"""

    def test_string_on_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("2", 5)

    def test_list_on_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([2, 3, 4, 5], 5)

    def test_float_on_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            b = Rectangle(3, 5, 8, 9)
            b.width = 3.6

    def test_boolean_on_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(False, 5)

    def test_tuples_on_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            b = Rectangle(5, 8, 9)
            b.width = (3, 4, 5)

    def test_dict_on_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({1: 2, 2: 3}, 5, 9, 3)

    def test_set_on_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({2, 7}, 5)

    def test_range_on_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(range(2), 5)

    def test_frozenset_on_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            b = Rectangle(4, 5, 7, 8)
            b.width = frozenset({"2", "3", "4"})

    def test_bytearray_on_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(bytearray(2), 5)

    def test_bytes_on_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(b"2", 5)

    def test_memoryview_on_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(memoryview(bytes(2)), 5)

    def test_None_on_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            b = Rectangle(5, 5)
            b.width = None

    def test_inf_on_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('inf'), 5, 3, 4)

    def test_nan_on_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('nan'), 5)

    def test_negative_on_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-9, 7, 6)

    def test_zero_on_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            b = Rectangle(2, 3, 4, 5)
            b.width = 0


class TestErrorTypesForHeight(unittest.TestCase):
    """This class is going to use the TestCase and check
       diffrent datatypes and the error they create"""

    def test_string_on_Height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            b = Rectangle(2, 5)
            b.height = "5"

    def test_list_on_Height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(6, [9, 7, 5], 9)

    def test_float_on_Height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            b = Rectangle(8, 9, 7)
            b.height = 6.9

    def test_boolean_on_Height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(6, True, 5)

    def test_tuples_on_Height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            b = Rectangle(5, 8, 9)
            b.height = (3, 4, 5)

    def test_dict_on_Height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, {1: 2, 2: 3}, 9)

    def test_set_on_Height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(6, {2, 7}, 7, 8)

    def test_range_on_Height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            b = Rectangle(2, 5, 8, 7)
            b.height = range(6)

    def test_frozenset_on_Height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            b = Rectangle(7, 7, 7, 8)
            b.height = frozenset({"5", "3"})

    def test_bytearray_on_Height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, bytearray(3), 7)

    def test_bytes_on_Height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            b = Rectangle(6, 8, 4)
            b.height = b"9"

    def test_memoryview_on_Height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(7, memoryview(bytes(8)), 9)

    def test_None_on_Height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, None, 9)

    def test_inf_on_Height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, float('inf'), 5, 3, 4)

    def test_nan_on_Height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(8, float('nan'), 5)

    def test_negative_on_Height(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            b = Rectangle(5, 9, 7, 6)
            b.height = -5

    def test_zero_on_Height(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(2, 0, 4, 5)


class TestErrorTypesForX(unittest.TestCase):
    """This class is going to use the TestCase and check
       diffrent datatypes and the error they create"""

    def test_string_on_X(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 5, "4")

    def test_list_on_X(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(6, 5, [3, 6], 9)

    def test_float_on_X(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 5, 7.8, 5)

    def test_boolean_on_X(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            b = Rectangle(5, 4, 1, 9)
            b.x = True

    def test_tuples_on_X(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            b = Rectangle(1, 2, 3, 4)
            b.x = (1, 5, 6)

    def test_dict_on_X(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(4, 6, {6: 7, 8: 9})

    def test_set_on_X(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            b = Rectangle(6, 2, 7, 7, 8)
            b.x = {5, 6}

    def test_range_on_X(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            b = Rectangle(2, 8, 7)
            b.x = range(6)

    def test_frozenset_on_X(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 6, frozenset({"5", "3"}), 9)

    def test_bytearray_on_X(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(5, 6, bytearray(3), 7)

    def test_bytes_on_X(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            b = Rectangle(5, 7, 5, 7)
            b.x = b"7"

    def test_memoryview_on_X(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(4, 8, memoryview(bytes(9)), 7)

    def test_None_on_X(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            b = Rectangle(5, 6, 9)
            b.x = None

    def test_inf_on_X(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(5, 4, float('inf'), 6, 4)

    def test_nan_on_X(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 8, float('nan'), 5, 9)

    def test_negative_on_X(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(5, 9, -7, 6)


class TestErrorTypesForY(unittest.TestCase):
    """This class is going to use the TestCase and check
       diffrent datatypes and the error they create"""

    def test_string_on_Y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 5, 8, "6")

    def test_list_on_Y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            b = Rectangle(6, 9, 7, 5, 9)
            b.y = [9, 8]

    def test_float_on_Y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(8, 9, 7, 8.9)

    def test_boolean_on_Y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            b = Rectangle(6, 6, 5, 9)
            b.y = False

    def test_tuples_on_Y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(5, 8, 9, (3, 4, 5), 8)

    def test_dict_on_Y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            b = Rectangle(5, 6, 2, 2, 9)
            b.y = {2: 4, 4: 6}

    def test_set_on_Y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(5, 1, 2, {3, 8, 6})

    def test_range_on_Y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 5, 8, range(7))

    def test_frozenset_on_Y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            b = Rectangle(1, 6, 8, 8)
            b.y = frozenset({"1", "2", "3"})

    def test_bytearray_on_Y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            b = Rectangle(53, 2, 4, 7)
            b.y = bytearray(4)

    def test_bytes_on_Y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 6, 5, b"8")

    def test_memoryview_on_Y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            b = Rectangle(7, 8, 9, 7)
            b.y = memoryview(bytes(6))

    def test_None_on_Y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 5, None, 6)

    def test_inf_on_Y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            b = Rectangle(4, 2, 5, 3, 4)
            b.y = float('inf')

    def test_nan_on_Y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 8, float('nan'), 5)

    def test_negative_on_Y(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(5, 9, 7, -6)
