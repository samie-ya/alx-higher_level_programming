#!/usr/bin/python3
"""Defining matrix_mul"""


def matrix_mul(m_a, m_b):
    if m_a = [] or m_a = [[]]:
        raise ValueError("m_a can't be empty")
    elif m_b = [] or m_b = [[]]:
        raise ValueError("m_b can't be empty")
    elif type(m_a) != list:
        raise TypeError("m_a must be a list")
    elif type(m_b) != list:
        raise TypeError("m_b must be a list")
