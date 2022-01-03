#!/usr/bin/python3
"""Unittest for the function and attribute in class Base"""


import unittest

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """This class is going to use the TestCase and check
       the function and attribute in class Base"""
    def test_public_id(self):
        b = Base()
        self.assertEqual(b.id, 1)

    def test_public_id_2(self):
        b = Base(12)
        self.assertEqual(b.id, 12)

    def test_public_id_3(self):
        b = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(b3.id, 3)

    def test_to_json_string(self):
        b = Rectangle(10, 7, 2, 8, 5)
        dic = b.to_dictionary()
        json_dict = Base.to_json_string([dic])
        self.assertEqual(json_dict, '[{"id": 5, "width": 10, "height": 7, "x": 2, "y": 8}]')

    def test_to_json_string_2(self):
        json_dict = Base.to_json_string([])
        self.assertEqual(json_dict, "[]")

    def test_to_json_string_3(self):
        json_dict = Base.to_json_string(None)
        self.assertEqual(json_dict, "[]")

    def test_to_json_string_4(self):
        s = Square(10, 7, 2, 8)
        dic = s.to_dictionary()
        json_dict = Base.to_json_string([dic])
        self.assertEqual(json_dict, '[{"id": 8, "size": 10, "x": 7, "y": 2}]')

    def test_to_json_string_5(self):
        b = Rectangle(10, 7, 2, 8, 5)
        dic = b.to_dictionary()
        json_dict = Base.to_json_string(dic)
        self.assertEqual(json_dict, '{"id": 5, "width": 10, "height": 7, "x": 2, "y": 8}')
