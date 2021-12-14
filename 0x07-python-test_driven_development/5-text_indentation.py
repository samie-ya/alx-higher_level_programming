#!/usr/bin/python3
"""Defining the function text_indentation"""


def text_indentation(text):
    """This function is used to find the character
       '?', '.' and ':' ina  astring and make newline twice
       when it find it in a string text

       Args:
           text (str): the string to be checked
    """
    if not(type(text) is str):
        raise TypeError("text must be a string")
    else:
        for i in range(len(text)):
            if (text[i] in "?.:"):
                text = text[:i + 1] + "\n\n" + text[i + 2:]
        print(text, end="")
