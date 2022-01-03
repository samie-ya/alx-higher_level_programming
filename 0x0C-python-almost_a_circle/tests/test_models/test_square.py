#!/usr/bin/python3
"""Unittest for the function and attribute in class Square"""

from io import StringIO
import unittest
from unittest.mock import patch

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """This class is going to use the TestCase and check
       the function and attribute in class Square"""

    def test_class(self):
        self.assertIs(type(Square), type(Base))

    def test_class2(self):
        self.assertIs(type(Square), type(Rectangle))

    def test_public_id_3(self):
        s = Square(1, 3, 5, 9)
        self.assertEqual(s.id, 9)

    def test_no_arguments(self):
        with self.assertRaises(TypeError):
            s = Square()

    def test_many_arguments(self):
        with self.assertRaises(TypeError):
            s = Square(1, 2, 4, 5, 6)

    def test_attributes(self):
        s = Square(1, 2, 3, 4)
        self.assertIs(s.size, 1)
        self.assertIs(s.x, 2)
        self.assertIs(s.y, 3)
        self.assertIs(s.id, 4)

    def test_attributes_2(self):
        s = Square(2, 3)
        s.size = 10
        s.x = 10
        s.y = 6
        s.id = 5
        self.assertIs(s.size, 10)
        self.assertIs(s.x, 10)
        self.assertIs(s.y, 6)
        self.assertIs(s.id, 5)

    def test_area(self):
        s = Square(5)
        self.assertEqual(s.area(), 25)

    def test_area(self):
        s = Square(3, 4, 5, 6)
        self.assertEqual(s.area(), 9)

    def test_area_with_argument(self):
        s = Square(4)
        with self.assertRaises(TypeError):
            s.area(1)

    def test_display(self):
        s = Square(3)
        on_screen = "###\n###\n###\n"
        with patch('sys.stdout', new=StringIO()) as f:
            s.display()
            self.assertEqual(f.getvalue(), on_screen)

    def test_display_2(self):
        s = Square(4)
        on_screen = "####\n####\n####\n####\n"
        with patch('sys.stdout', new=StringIO()) as f:
            s.display()
            self.assertEqual(f.getvalue(), on_screen)

    def test_display_with_x_and_y(self):
        s = Square(2, 3, 4, 5)
        on_screen = "\n\n\n\n   ##\n   ##\n"
        with patch('sys.stdout', new=StringIO()) as f:
            s.display()
            self.assertEqual(f.getvalue(), on_screen)

    def test_display_with_argument(self):
        s = Square(2)
        with self.assertRaises(TypeError):
            s.display(3)

    def test_str_(self):
        s = Square(2, 2, 2, 2)
        self.assertEqual(str(s), "[Square] (2) 2/2 - 2")

    def test_str_2(self):
        s = Square(1, 2, 3, 5)
        s1 = Square(2, 3, 4, 6)
        self.assertEqual(str(s1), "[Square] (6) 3/4 - 2")

    def test_str_3(self):
        s = Square(2, 4, 6, 8)
        with self.assertRaises(TypeError):
            s.__str__(1)

    def test_update(self):
        s = Square(10, 9, 8, 7)
        s.update()
        self.assertEqual(str(s), "[Square] (7) 9/8 - 10")
        s.update(89)
        self.assertEqual(str(s), "[Square] (89) 9/8 - 10")
        s.update(89, 90)
        self.assertEqual(str(s), "[Square] (89) 9/8 - 90")
        s.update(89, 90, 91)
        self.assertEqual(str(s), "[Square] (89) 91/8 - 90")
        s.update(89, 90, 91, 92)
        self.assertEqual(str(s), "[Square] (89) 91/92 - 90")

    def test_update_kwagrs(self):
        s = Square(10, 9, 8, 7)
        s.update()
        self.assertEqual(str(s), "[Square] (7) 9/8 - 10")
        s.update(x=5)
        self.assertEqual(str(s), "[Square] (7) 5/8 - 10")
        s.update(x=2, y=3)
        self.assertEqual(str(s), "[Square] (7) 2/3 - 10")
        s.update(x=3, id=5, y=4)
        self.assertEqual(str(s), "[Square] (5) 3/4 - 10")
        s.update(x=4, size=5, y=6, id=7)
        self.assertEqual(str(s), "[Square] (7) 4/6 - 5")

    def test_to_dictionary(self):
        s = Square(10, 9, 8, 7)
        s1 = s.to_dictionary()
        self.assertEqual(s1, {'id': 7, 'size': 10, 'x': 9, 'y': 8})

    def test_to_dictionary_2(self):
        s = Square(1, 1, 1, 1)
        s1 = s.to_dictionary()
        self.assertEqual(s1, {'id': 1, 'size': 1, 'x': 1, 'y': 1})

    def test_to_dictionary_3(self):
        s = Square(1, 2, 3, 4)
        with self.assertRaises(TypeError):
            s.to_dictionary(3)


class TestErrorInTypesForSize(unittest.TestCase):
    """This class is going to use the TestCase and check
       diffrent datatypes and the error they create"""

    def test_string_on_Size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("2", 5)

    def test_list_on_Size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square([2, 3, 4, 5], 5)

    def test_float_on_Size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s = Square(3, 5, 8, 9)
            s.size = 3.6

    def test_boolean_on_Size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(False, 5)

    def test_tuples_on_Size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s = Square(5, 8, 9)
            s.size = (3, 4, 5)

    def test_dict_on_Size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({1: 2, 2: 3}, 5, 9, 3)

    def test_set_on_Size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({2, 7}, 5)

    def test_range_on_Size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(range(2), 5)

    def test_frozenset_on_Size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s = Square(4, 5, 7, 8)
            s.size = frozenset({"2", "3", "4"})

    def test_bytearray_on_Size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(bytearray(2), 5)

    def test_bytes_on_Size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(b"2", 5)

    def test_memoryview_on_Size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(memoryview(bytes(2)), 5)

    def test_None_on_Size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s = Square(5, 5)
            s.size = None

    def test_inf_on_Size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(float('inf'), 5, 3, 4)

    def test_nan_on_Size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(float('nan'), 5)

    def test_negative_on_Size(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-9, 7, 6)

    def test_zero_on_Size(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s = Square(2, 3, 4, 5)
            s.size = 0


class TestErrorTypesForX(unittest.TestCase):
    """This class is going to use the TestCase and check
       diffrent datatypes and the error they create"""

    def test_string_on_X(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(5, "4")

    def test_list_on_X(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(6, [3, 6], 9)

    def test_float_on_X(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, 7.8, 5)

    def test_boolean_on_X(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s = Square(5, 4, 1, 9)
            s.x = True

    def test_tuples_on_X(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s = Square(1, 2, 3, 4)
            s.x = (1, 5, 6)

    def test_dict_on_X(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(6, {6: 7, 8: 9})

    def test_set_on_X(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s = Square(6, 2, 7, 8)
            s.x = {5, 6}

    def test_range_on_X(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s = Square(2, 8, 7)
            s.x = range(6)

    def test_frozenset_on_X(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(6, frozenset({"5", "3"}), 9)

    def test_bytearray_on_X(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(5, bytearray(3), 7)

    def test_bytes_on_X(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s = Square(5, 7, 5, 7)
            s.x = b"7"

    def test_memoryview_on_X(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(8, memoryview(bytes(9)), 7)

    def test_None_on_X(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s = Square(5, 6, 9)
            s.x = None

    def test_inf_on_X(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(5, float('inf'), 6, 4)

    def test_nan_on_X(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, float('nan'), 5, 9)

    def test_negative_on_X(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(5, -7, 6, 7)


class TestErrorTypesForY(unittest.TestCase):
    """This class is going to use the TestCase and check
       diffrent datatypes and the error they create"""

    def test_string_on_Y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 8, "6")

    def test_list_on_Y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s = Square(6, 7, 5, 9)
            s.y = [9, 8]

    def test_float_on_Y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(8, 7, 8.9, 9)

    def test_boolean_on_Y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s = Square(6, 6, 5, 9)
            s.y = False

    def test_tuples_on_Y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(5, 9, (3, 4, 5), 8)

    def test_dict_on_Y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s = Square(5, 2, 2, 9)
            s.y = {2: 4, 4: 6}

    def test_set_on_Y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(5, 1, {3, 8, 6})

    def test_range_on_Y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(5, 8, range(7), 9)

    def test_frozenset_on_Y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s = Square(1, 6, 8, 8)
            s.y = frozenset({"1", "2", "3"})

    def test_bytearray_on_Y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s = Square(53, 2, 4, 7)
            s.y = bytearray(4)

    def test_bytes_on_Y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 6, b"8", 7)

    def test_memoryview_on_Y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s = Square(7, 8, 9, 7)
            s.y = memoryview(bytes(6))

    def test_None_on_Y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 5, None, 6)

    def test_inf_on_Y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s = Square(4, 2, 3, 4)
            s.y = float('inf')

    def test_nan_on_Y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 8, float('nan'), 5)

    def test_negative_on_Y(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(5, 9, -6, 8)
