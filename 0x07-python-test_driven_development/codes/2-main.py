#!/usr/bin/python3
matrix_divided = __import__('2-matrix_divided').matrix_divided

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(matrix_divided(matrix, 3))
print(matrix)

try:
    matrix = [
    [1, 2, 3, 10],
    [4, 5, 6],
    [7, 8, 9],
    [3, 4, 5]
    ]
    print(matrix_divided(matrix, 5))
except Exception as e:
    print(e)
