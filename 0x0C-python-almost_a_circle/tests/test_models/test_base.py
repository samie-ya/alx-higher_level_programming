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
