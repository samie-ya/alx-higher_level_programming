#!/usr/bin/python3


def remove_char_at(str, n):
    new_str = str[:]
    if n < 0 or n >= len(str):
        return new_str
    else:
        for i in range(len(str)):
            if i == n:
                new_str = new_str[0:i] + new_str[i + 1:]
        return new_str
